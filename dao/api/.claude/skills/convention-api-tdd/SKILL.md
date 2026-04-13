---
name: convention-api-tdd
description: API 레이어 TDD 규칙 (pytest + httpx)
---

# API TDD

## 프레임워크
- **pytest** + **httpx** (AsyncClient)

## 구조
- `tests/` = `app/` 미러
- `tests/domains/auth/test_router.py`
- `tests/domains/auth/test_service.py`

## TDD 사이클
1. Red → Green → Refactor

## 테스트 패턴

### Router 테스트 (통합)
```python
async def test_create_device_returns_201(client: AsyncClient):
    response = await client.post("/api/devices", json={
        "name": "switch-01", "ipAddress": "10.0.0.1", "deviceTypeId": 1
    })
    assert response.status_code == 201
    assert response.json()["name"] == "switch-01"
```

### Service 테스트 (단위)
```python
def test_device_service_raises_on_duplicate_ip(mock_repo):
    mock_repo.find_by_ip.return_value = existing_device
    with pytest.raises(ConflictError):
        service.create_device(DeviceCreate(name="x", ip_address="10.0.0.1"))
```

## Fixture 패턴

```python
@pytest.fixture
async def client(app):
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c

@pytest.fixture
def mock_repo():
    return MagicMock(spec=DeviceRepository)
```

## Mock 전략
- DB: 테스트용 PostgreSQL (testcontainers) 또는 SQLite
- ClickHouse: mock client
- 외부 API: httpx MockTransport

## 커버리지
- `pytest --cov=app tests/`
