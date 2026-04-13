---
name: convention-backend-tdd
description: FastAPI 백엔드 TDD 워크플로우
---

# TDD Convention (Backend)

## 워크플로우
1. 실패하는 테스트 작성
2. 테스트를 통과하는 최소 구현
3. 리팩터링 (테스트 유지)

## 테스트 구조
- tests/ 디렉토리는 app/ 미러 구조
- 파일명: `test_{모듈명}.py`
- 함수명: `test_{행위}_{조건}_{기대결과}()`

## 픽스처 패턴

```python
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c

@pytest.fixture
def sample_user():
    return {"name": "홍길동", "email": "hong@example.com"}
```

## 테스트 레이어
- Unit: services, repositories 개별 테스트 (의존성 mock)
- Integration: 라우터 → 서비스 → DB 통합 테스트
- conftest.py에 공통 픽스처 정의

## 실행

```bash
pytest tests/ -v                          # 전체
pytest tests/domains/user/ -v             # 도메인별
pytest tests/domains/user/test_services.py::test_name -v  # 단건
```
