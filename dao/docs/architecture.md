# DAO Observability Platform — Architecture

## 데이터 흐름

```
[디바이스/서버/앱]
    ↓ SNMP / OTLP
[collector (Go)] → MetricParser → LogParser → DeviceResolver → EventDetect → Batch
    ↓ Kafka (metrics, logs, traces, events 토픽)
[consumer (Python)] → Validate → Batch → Bulk INSERT
    ↓
[ClickHouse (시계열 OLAP)] + [PostgreSQL (마스터 OLTP)] + [Redis (캐시)]
    ↓
[api (FastAPI)] → REST API
    ↓
[Nginx :80] → /api/* → api:8000 | /* → web:3000
    ↓
[web (React SPA)]
```

## Collector (Go 1.24)

OTel Collector Builder(OCB)로 빌드한 커스텀 바이너리.

### 프로세서 파이프라인 순서
1. **MetricParser** — SNMP OID→metric_name, 단위 정규화, delta 계산
2. **LogParser** — RFC3164/5424, JSON, vendor 포맷→통합 스키마
3. **Filter** — 불필요 메트릭/로그 드롭 (30-70% 트래픽 감소)
4. **Transform** — 속성 정규화, PII 마스킹
5. **Batch** — 100건 또는 5초 timeout
6. **DeviceResolver** — IP→device_id (PostgreSQL + in-memory cache TTL 5분)
7. **EventDetect** — 임계치 위반→events 토픽
8. **Kafka Exporter** — 메인 출력

### 라이브러리
- franz-go (Kafka), pgx (PostgreSQL), zerolog, spf13/viper

## Kafka (KRaft 4.0)

| 토픽 | Key | 파티션 | 보관 |
|------|-----|--------|------|
| metrics | device_id | 4 | 90일 |
| logs | device_id | 4 | 30일 |
| traces | trace_id | 4 | 14일 |
| events | device_id | 2 | 7일 |

## Consumer (Python 3.13)

토픽별 독립 바이너리 4개:

| 바이너리 | 입력 토픽 | 출력 | 배치 |
|----------|----------|------|------|
| metrics-consumer | metrics | ClickHouse dao.metric | 5000건/5초 |
| logs-consumer | logs | ClickHouse dao.log | 5000건/5초 |
| traces-consumer | traces | ClickHouse dao.trace_span | 5000건/5초 |
| events-consumer | events | PostgreSQL alert_history | 즉시 |

### 라이브러리
- confluent-kafka, clickhouse-connect, pydantic, structlog

## Storage

### ClickHouse (시계열 OLAP)
- `dao.metric` — MergeTree, TTL 90일
- `dao.log` — MergeTree, TTL 30일
- `dao.trace_span` — MergeTree, TTL 14일
- `dao.dim_device` — ReplacingMergeTree (PG 동기화)

### PostgreSQL (마스터 OLTP)
- `role` — RBAC (admin, operator, viewer)
- `users` — 사용자 + 서비스 계정
- `groups` — 계층 구조 (Closure Table)
- `device` — 모니터링 대상 장비
- `alert_history` — 알림 이력

### Redis
- DeviceResolver IP 캐시 (TTL 5분)
- 사용자 세션
- 쿼리 결과 캐시

## API (FastAPI)

| 도메인 | Prefix | 핵심 기능 |
|--------|--------|----------|
| Auth | `/api/auth` | JWT 로그인, 토큰 갱신 |
| Admin | `/api/admin` | 사용자/역할/그룹 CRUD |
| Asset | `/api/devices` | 장비/인터페이스/정책 |
| Query | `/api/metrics`, `/logs`, `/traces` | 시계열 조회, 로그 검색 |
| Alert | `/api/alerts` | 알림 규칙/이력/채널 |
| Report | `/api/reports` | PDF 리포트 |

### 라이브러리
- FastAPI, SQLAlchemy 2.0, Pydantic 2, PyJWT, clickhouse-connect, structlog

## Web (React 19)

### 주요 페이지
- Dashboard — 실시간 메트릭 차트 (Recharts)
- Device List — 장비 관리 CRUD
- Log Explorer — 로그 검색 + WebSocket 스트리밍
- Trace View — 분산 트레이스 워터폴
- Alert Management — 규칙/이력 관리
- Settings — 사용자/역할 관리

### 라이브러리
- React 19, TypeScript 6, Vite, Zustand, Recharts, D3.js, Axios, dayjs

## Gateway (Nginx)

- 단일 포트 :80
- `/api/*` → api:8000
- `/*` → web:3000 (SPA)
- SSL/TLS termination
