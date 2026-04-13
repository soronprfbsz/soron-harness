---
paths:
  - "collector/**"
---

# Collector Conventions (Go)

Go 기반 OTel Collector. 상세 스킬 참조:
- [네이밍](collector/.claude/skills/convention-collector-naming/SKILL.md)
- [프로젝트 구조](collector/.claude/skills/convention-collector-project-structure/SKILL.md)
- [OTel 패턴](collector/.claude/skills/convention-collector-otel/SKILL.md)
- [Kafka Producer](collector/.claude/skills/convention-collector-kafka-producer/SKILL.md)
- [Git](.claude/skills/convention-git/SKILL.md)
- [Code Review](.claude/skills/convention-code-review/SKILL.md)

## 핵심 요약

### 네이밍
- 파일: `snake_case.go` | 패키지: lowercase 단일단어
- Public: `PascalCase` | Private: `camelCase`
- 생성자: `New{Type}` | 인터페이스: `{동사}er`
- 에러: `Err{Name}` | 약어: 전체 대문자 (`HTTPClient`)
- JSON 태그: `camelCase`

### 구조
- `cmd/collector/main.go` → `internal/{receiver,processor,exporter,config}`
- 의존: receiver → processor → exporter (단방향)

### Kafka Producer
- Key: `device_id`, Value: JSON, 배치: 100건/5초

### 에러/로깅
- `fmt.Errorf("component: %w", err)` 래핑, 최상위에서만 로깅
- zerolog, JSON, stdout, UTC
