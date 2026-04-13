---
name: convention-backend-database
description: PostgreSQL 데이터베이스 네이밍 컨벤션
---

# Database Naming Convention

## 1. 기본 원칙

| 규칙 | 예시 | 비고 |
|------|------|------|
| **소문자만 사용** | `users`, `audit_log` | PostgreSQL은 unquoted identifier를 자동 lowercase 변환 |
| **snake_case 사용** | `created_at`, `user_group` | camelCase, PascalCase 금지 |
| **테이블명 단수형** | `role`, `permission`, `audit_log` | 예약어인 경우만 복수형 허용 (아래 예외 참고) |
| **컬럼명 단수형** | `role_id`, `device_id` | 예외 없이 단수형 |
| **약어 지양, 풀네임 사용** | `description` (O), `desc` (X) | `i18n`, `l10n` 등 보편적 약어만 예외 |

## 2. 예약어 복수형 예외

단수형이 PostgreSQL 예약어인 경우 **복수형으로 회피**. 따옴표(`"user"`)로 감싸는 방식은 금지.

| 단수형 문제 | 채택 | 근거 |
|------------|------|------|
| `user`는 예약어 (`SELECT user` → 현재 사용자 반환) | **`users`** | 복수형은 예약어가 아님 |
| `group`은 예약어 (`GROUP BY`) | **`groups`** | 복수형은 예약어가 아님 |
| `order`는 예약어 (`ORDER BY`) | **`orders`** | 복수형은 예약어가 아님 |

## 3. Primary Key / Foreign Key

### PK: `id` 사용 (테이블명 접두사 없음)

```sql
-- O
CREATE TABLE role (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid()
);

-- X
CREATE TABLE role (
    role_id UUID PRIMARY KEY DEFAULT gen_random_uuid()
);
```

### FK: `{entity}_id` 사용

참조 대상 엔티티의 **단수형** + `_id`. 테이블명이 복수형(예외)이더라도 FK는 단수형.

```sql
CREATE TABLE audit_log (
    user_id UUID REFERENCES users(id),  -- FK: 단수형 (user)
    role_id UUID REFERENCES role(id)
);
```

### 자기참조 FK

단순 1-depth 자기참조: `parent_id`

```sql
parent_id UUID REFERENCES groups(id)
```

계층구조가 필요한 경우 Closure Table 패턴 검토: `{entity}_hierarchy`

## 4. 컬럼 네이밍

### Boolean: `is_` / `has_` / `can_` 접두사

```sql
is_active    BOOLEAN DEFAULT false,   -- 상태/속성
has_mfa      BOOLEAN DEFAULT false,   -- 보유 여부
can_login    BOOLEAN DEFAULT true,    -- 능력/허용 여부
```

### 날짜/시간: `_at` / `_on` 접미사

| 접미사 | 용도 | 타입 | 예시 |
|--------|------|------|------|
| `_at` | 정확한 시점 (타임스탬프) | `TIMESTAMPTZ` | `created_at`, `expires_at` |
| `_on` | 날짜만 (시간 불필요) | `DATE` | `birth_on`, `hired_on` |

`TIMESTAMPTZ`를 기본으로 사용하므로 **`_at` 접미사가 표준**.

### 금액/수량: 단위 명시

```sql
duration_sec       INTEGER,   -- 초 단위
timeout_min        INTEGER,   -- 분 단위
retention_day      INTEGER,   -- 일 단위
cpu_usage_percent  BIGINT,    -- 퍼센트 단위
```

### 상태/분류: `status` 또는 `type`

```sql
status  VARCHAR(16) DEFAULT 'active',   -- 소문자 snake_case 값
type    VARCHAR(32),
```

## 5. 매핑(Junction) 테이블

N:M 관계의 중간 테이블은 **두 엔티티명을 `_`로 결합** (단수형).

```sql
user_group         -- users ↔ groups
role_permission    -- role ↔ permission
```

매핑 테이블의 컬럼은 양쪽 FK + 필요 시 메타 컬럼(`joined_at` 등).

## 6. 제약조건(Constraint) 네이밍

자동 생성 이름에 의존하지 않고 명시적으로 네이밍.

| 유형 | 패턴 | 예시 |
|------|------|------|
| Primary Key | `pk_{table}` | `pk_users` |
| Foreign Key | `fk_{table}_{참조table}` | `fk_users_role` |
| Unique | `uq_{table}_{column}` | `uq_users_email` |
| Unique (복합) | `uq_{table}_{col1}_{col2}` | `uq_role_permission_role_id_permission_id` |
| Check | `ck_{table}_{column}_{설명}` | `ck_users_status_valid` |

## 7. 인덱스(Index) 네이밍

| 유형 | 패턴 | 예시 |
|------|------|------|
| 일반 인덱스 | `idx_{table}_{column}` | `idx_audit_log_created_at` |
| 복합 인덱스 | `idx_{table}_{col1}_{col2}` | `idx_audit_log_resource_resource_id` |
| 부분 인덱스 | `idx_{table}_{column}_{조건}` | `idx_users_email_active` |

## 8. Enum / 상태값

소문자 snake_case로 통일.

```sql
-- VARCHAR 기반
status VARCHAR(16) CHECK (status IN ('active', 'inactive', 'locked', 'pending'))

-- PostgreSQL ENUM 타입: {테이블}_{컬럼} 패턴
CREATE TYPE user_status AS ENUM ('active', 'inactive', 'locked', 'pending');
```

## 9. COMMENT 작성 규칙

모든 테이블과 컬럼에 `COMMENT ON` 작성.

```sql
COMMENT ON TABLE role IS '역할 정의';
COMMENT ON COLUMN role.id IS '역할 고유 식별자 (UUID v4)';
COMMENT ON COLUMN role.status IS '상태 (active|inactive)';
```

| 규칙 | 설명 |
|------|------|
| 한 줄로 작성 | 간결하게 핵심만 기술 |
| 허용값 명시 | 상태/분류 컬럼은 괄호 안에 허용값 나열 |
| FK 관계 명시 | `'소유자 FK (users.id)'` 형태로 참조 대상 표기 |
| 스키마 변경 시 함께 갱신 | 의미 변경 시 반드시 업데이트 |

## 10. 금지 사항

| 항목 | 금지 예시 | 올바른 예시 |
|------|----------|------------|
| 대문자 / camelCase | `userId`, `UserName` | `user_id`, `username` |
| 헝가리안 표기법 | `tbl_users`, `col_name` | `users`, `name` |
| 의미 없는 약어 | `usr`, `grp`, `pwd`, `desc` | `users`, `groups`, `password_hash`, `description` |
| 예약어 (단수형) 사용 | `user`, `order`, `group` | `users`, `orders`, `groups` (복수형 회피) |
| PK에 테이블명 접두사 | `users.user_id` (PK) | `users.id` (PK) |
| Boolean에 접두사 누락 | `active`, `deleted` | `is_active`, `is_deleted` |
| 날짜에 접미사 누락 | `last_login`, `created` | `last_login_at`, `created_at` |
| 따옴표 감싸기 | `"user"`, `"group"` | `users`, `groups` (복수형 회피) |

## 체크리스트

새로운 테이블/컬럼 추가 시 확인:

- [ ] 소문자 + snake_case인가?
- [ ] 테이블명이 단수형인가? (예약어 예외만 복수형)
- [ ] PK는 `id`, FK는 `{참조테이블}_id` 패턴인가?
- [ ] Boolean에 `is_` / `has_` / `can_` 접두사가 있는가?
- [ ] 타임스탬프에 `_at` 접미사가 있는가?
- [ ] 의미 없는 약어를 쓰지 않았는가?
- [ ] 제약조건/인덱스에 명시적 이름을 부여했는가?
- [ ] 테이블과 모든 컬럼에 COMMENT을 작성했는가?
- [ ] 상태/분류값이 소문자 snake_case인가?
