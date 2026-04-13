---
paths:
  - "consumer/**"
---

# Consumer Conventions (Python)

Kafka → ClickHouse/PG 적재. 상세 스킬 참조:
- [네이밍](consumer/.claude/skills/convention-consumer-naming/SKILL.md)
- [프로젝트 구조](consumer/.claude/skills/convention-consumer-project-structure/SKILL.md)
- [Kafka Consumer](consumer/.claude/skills/convention-consumer-kafka/SKILL.md)
- [ClickHouse](consumer/.claude/skills/convention-consumer-clickhouse/SKILL.md)
- [TDD](consumer/.claude/skills/convention-consumer-tdd/SKILL.md)
- [Git](.claude/skills/convention-git/SKILL.md)
- [Code Review](.claude/skills/convention-code-review/SKILL.md)

## 핵심 요약

### 네이밍
- 파일/변수/함수: `snake_case` | 클래스: `PascalCase`
- 상수: `UPPER_SNAKE_CASE` | Boolean: `is_`/`has_`/`can_`

### 구조
- `src/{consumers,writers,validators,common}` → `tests/` (src 미러)
- 의존: consumers → validators → writers (단방향)

### Kafka Consumer
- Group ID: `obsv-{topic}-consumer`, auto.commit: `False`, 수동 커밋
- 배치: 5,000건/5초, 검증 실패 시 메시지 드롭

### ClickHouse
- clickhouse-connect, 벌크 INSERT, column_names 필수
