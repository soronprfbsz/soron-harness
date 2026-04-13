---
name: convention-collector-project-structure
description: Go Collector 프로젝트 디렉토리 구조
---

# Collector 프로젝트 구조

```
collector/
├── cmd/
│   └── collector/
│       └── main.go              # 엔트리포인트
├── internal/                    # 외부 비공개
│   ├── receiver/                # 데이터 수신
│   │   ├── snmp/                # SNMP (표준 + 커스텀 MIB)
│   │   └── otlp/                # OTLP gRPC/HTTP
│   ├── processor/               # 가공 파이프라인
│   │   ├── metricparser/        # OID→metric_name, 단위 정규화
│   │   ├── logparser/           # syslog/JSON→통합 스키마
│   │   ├── deviceresolver/      # IP→device_id (PG + cache)
│   │   ├── eventdetect/         # 임계치 위반→events 토픽
│   │   └── schemanorm/          # 속성명·단위 표준화
│   ├── exporter/
│   │   └── kafka/               # Kafka 발행 (franz-go)
│   └── config/                  # 설정 (viper)
├── pkg/                         # 외부 공개 유틸
├── go.mod
├── go.sum
├── Makefile
└── Dockerfile
```

## 의존 방향

```
receiver → processor → exporter (단방향)
config는 모든 레이어에서 import 가능
```

- receiver는 processor를 직접 import하지 않음 (채널/인터페이스로 연결)
- processor 간 의존은 파이프라인 순서만 허용
- exporter는 receiver/processor를 import하지 않음
- `internal/` 외부 노출 금지, `pkg/` 만 공개
