---
name: convention-consumer-project-structure
description: Python Consumer 프로젝트 디렉토리 구조
---

# Consumer 프로젝트 구조

```
consumer/
├── src/
│   ├── __init__.py
│   ├── main.py                  # CLI 엔트리 (--topic metrics|logs|traces|events)
│   ├── consumers/               # Kafka 소비자 (토픽별)
│   │   ├── __init__.py
│   │   ├── base.py              # BaseConsumer ABC
│   │   ├── metrics_consumer.py
│   │   ├── logs_consumer.py
│   │   ├── traces_consumer.py
│   │   └── events_consumer.py
│   ├── writers/                 # DB 적재
│   │   ├── __init__.py
│   │   ├── clickhouse_writer.py
│   │   └── postgres_writer.py
│   ├── validators/              # 스키마 검증
│   │   ├── __init__.py
│   │   └── schema.py
│   └── common/                  # 공통
│       ├── __init__.py
│       ├── config.py            # pydantic-settings
│       └── logging.py           # structlog
├── tests/                       # src/ 미러
│   ├── consumers/
│   ├── writers/
│   └── validators/
├── pyproject.toml
├── Dockerfile
└── Makefile
```

## 의존 방향

```
consumers → validators → writers (단방향)
common은 모든 모듈에서 import 가능
```

- consumers/는 writers/를 직접 호출하지 않음 (BaseConsumer 인터페이스)
- validators/는 writers/를 import하지 않음
- writers/는 consumers/를 import하지 않음

## 패키지 관리
- uv (pyproject.toml + uv.lock)
- .venv 프로젝트 루트
