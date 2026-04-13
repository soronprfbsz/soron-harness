---
name: convention-collector-otel
description: OTel Collector 컴포넌트 패턴 (Receiver/Processor/Exporter)
---

# OTel Collector 패턴

## Component 인터페이스

각 컴포넌트는 OTel Collector SDK 인터페이스를 구현:

```go
// Receiver — 데이터 수신
type Receiver interface {
    Start(ctx context.Context, host component.Host) error
    Shutdown(ctx context.Context) error
}

// Processor — 데이터 가공
type Processor interface {
    ProcessMetrics(ctx context.Context, md pmetric.Metrics) (pmetric.Metrics, error)
    ProcessLogs(ctx context.Context, ld plog.Logs) (plog.Logs, error)
}

// Exporter — 데이터 출력
type Exporter interface {
    ConsumeMetrics(ctx context.Context, md pmetric.Metrics) error
    ConsumeLogs(ctx context.Context, ld plog.Logs) error
    Shutdown(ctx context.Context) error
}
```

## Factory 패턴

각 컴포넌트는 Factory 함수로 생성:

```go
func NewFactory() receiver.Factory {
    return receiver.NewFactory(
        metadata.Type,
        createDefaultConfig,
        receiver.WithMetrics(createMetricsReceiver, metadata.MetricsStability),
    )
}

func createDefaultConfig() component.Config {
    return &Config{
        Interval: 60 * time.Second,
    }
}
```

## 프로세서 파이프라인

순서 고정: MetricParser → LogParser → Filter → Transform → Batch → DeviceResolver → EventDetect → Kafka

각 프로세서는 독립적으로 테스트 가능해야 한다.

## 설정

- spf13/viper 사용
- 환경변수: `OBSV_COLLECTOR_` prefix
- 설정 파일: `config.yaml`
- 우선순위: 환경변수 > 설정파일 > 기본값
