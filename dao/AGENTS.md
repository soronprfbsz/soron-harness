# DAO Observability Platform

온프레미스 IT 인프라 옵저버빌리티 플랫폼. 메트릭·로그·트레이스 수집 → 분석 → 시각화 → 알림.

## 아키텍처

→ [docs/architecture.md](docs/architecture.md)

## 레이어

| 레이어 | 디렉토리 | 기술 | Rule (자동 주입) |
|--------|----------|------|-----------------|
| Collector | `collector/` | Go 1.24, OTel Collector | [convention-collector](.claude/rules/convention-collector.md) |
| Consumer | `consumer/` | Python 3.13, confluent-kafka | [convention-consumer](.claude/rules/convention-consumer.md) |
| API | `api/` | Python 3.13, FastAPI | [convention-api](.claude/rules/convention-api.md) |
| Web | `web/` | React 19, TypeScript 6, Vite | [convention-web](.claude/rules/convention-web.md) |
| Infra | `infra/` | Docker Compose | — |

## 컨벤션 자동 주입

`.claude/hooks/pre_write.py`가 파일 경로를 감지하여 해당 Rule을 자동 주입한다.

| 경로 패턴 | 주입 Rule | 레이어 Skills |
|----------|----------|--------------|
| `collector/**/*.go` | convention-collector | [naming](collector/.claude/skills/convention-naming/SKILL.md) · [structure](collector/.claude/skills/convention-project-structure/SKILL.md) · [otel](collector/.claude/skills/convention-otel/SKILL.md) · [kafka-producer](collector/.claude/skills/convention-kafka-producer/SKILL.md) |
| `consumer/**/*.py` | convention-consumer | [naming](consumer/.claude/skills/convention-naming/SKILL.md) · [structure](consumer/.claude/skills/convention-project-structure/SKILL.md) · [kafka-consumer](consumer/.claude/skills/convention-kafka-consumer/SKILL.md) · [clickhouse](consumer/.claude/skills/convention-clickhouse/SKILL.md) · [tdd](consumer/.claude/skills/convention-tdd/SKILL.md) |
| `api/**/*.py` | convention-api | [naming](api/.claude/skills/convention-naming/SKILL.md) · [structure](api/.claude/skills/convention-project-structure/SKILL.md) · [api-design](api/.claude/skills/convention-api-design/SKILL.md) · [database](api/.claude/skills/convention-database/SKILL.md) · [tdd](api/.claude/skills/convention-tdd/SKILL.md) |
| `web/**/*.{ts,tsx}` | convention-web | [naming](web/.claude/skills/convention-naming/SKILL.md) · [structure](web/.claude/skills/convention-project-structure/SKILL.md) · [component](web/.claude/skills/convention-component/SKILL.md) · [state](web/.claude/skills/convention-state/SKILL.md) · [tdd](web/.claude/skills/convention-tdd/SKILL.md) |

### 공통 Skills
- [Git](.claude/skills/convention-git/SKILL.md)
- [Code Review](.claude/skills/convention-code-review/SKILL.md)
- [공통 컨벤션](.claude/skills/convention-common/SKILL.md) (DateTime, 로깅, DB 네이밍)

## 인프라 커맨드

```bash
make infra-up       # 서비스 기동 (Kafka, CH, PG, Redis)
make infra-down     # 중지
make check          # 연결 점검
make status         # 상태 확인
make pg-cli         # PostgreSQL CLI
make ch-cli         # ClickHouse CLI
```

## 개발 커맨드

| Collector | Consumer | API | Web |
|-----------|----------|-----|----------|
| `go build ./cmd/collector` | `python -m src.main --topic metrics` | `uvicorn app.main:app --reload` | `npm run dev` |
| `go test ./...` | `pytest tests/ -v` | `pytest tests/ -v` | `npm test` |
| `go vet ./...` | `ruff check . && mypy src/` | `ruff check . && mypy app/` | `npx tsc -b` |

## 파이프라인 테스트

```bash
make test-produce    # 샘플 메트릭 → Kafka
make test-consume    # Kafka → ClickHouse
make test-pipeline   # 전체 (produce → consume → verify)
make test-verify     # ClickHouse 확인
```

## Key Decisions

- Write/Read 분리: Collector→Kafka→Consumer (쓰기) / API→ClickHouse (읽기)
- 단일 API 서버 (마이크로서비스 아님)
- DeviceResolver: IP→device_id (PG + Redis 캐시 TTL 5분)
- DateTime: UTC 저장, ISO 8601
- JSON Logging: structlog (Python), zerolog (Go)
- Python 패키지: uv
- RBAC: Super Admin / Admin / Operator / Viewer
