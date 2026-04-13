---
name: convention-collector-naming
description: Go 네이밍 컨벤션 (Collector 레이어)
---

# Go 네이밍 규칙

| 대상 | 규칙 | 예시 |
|------|------|------|
| 파일 | snake_case.go | `metric_parser.go`, `device_resolver.go` |
| 패키지 | lowercase 단일단어 (밑줄 없음) | `metricparser`, `deviceresolver` |
| Public 식별자 | PascalCase | `MetricParser`, `NewCollector` |
| Private 식별자 | camelCase | `parseOID`, `batchSize` |
| 생성자 | `New{Type}` | `NewMetricParser(cfg Config)` |
| 인터페이스 | `{동사}er` | `Receiver`, `Processor`, `Exporter` |
| 에러 (public) | `Err{Name}` | `ErrDeviceNotFound` |
| 에러 (private) | `err{name}` | `errInvalidOID` |
| 상수 (public) | PascalCase | `DefaultBatchSize`, `MaxRetries` |
| 상수 (private) | camelCase | `defaultTimeout` |
| 약어 | 전체 대문자 또는 전체 소문자 | `HTTPClient` (O), `HttpClient` (X) |
| JSON 태그 | camelCase | `` `json:"deviceId"` `` |
| Enum | iota + Type 정의 | `type Severity int` |

## 규칙

- 의미 없는 이름 금지 (`data`, `result`, `temp`)
- 단일 문자 변수 금지 (루프 `i`, `j`, `k` 제외)
- 약어는 표준만 허용 (HTTP, UUID, API, SNMP, OID, OTLP)
- 양성 Boolean (`isActive`, not `isNotActive`)
- Getter에 `Get` 접두사 불필요 (`Name()`, not `GetName()`)
