---
name: convention-frontend-tdd
description: React 프론트엔드 TDD 워크플로우
---

# TDD Convention (Frontend)

## 워크플로우
1. 실패하는 테스트 작성
2. 테스트를 통과하는 최소 구현
3. 리팩터링 (테스트 유지)

## 도구
- 테스트 러너: vitest
- 컴포넌트 테스트: React Testing Library
- 사용자 이벤트: @testing-library/user-event

## 테스트 작성 원칙
- 사용자 행위 중심: 구현 세부사항이 아닌 사용자가 보는 것을 테스트
- getByRole, getByText 우선 (getByTestId는 최후 수단)

## 테스트 패턴

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { UserCard } from "./UserCard";

describe("UserCard", () => {
  it("사용자 이름을 표시한다", () => {
    render(<UserCard user={{ name: "홍길동" }} />);
    expect(screen.getByText("홍길동")).toBeInTheDocument();
  });

  it("클릭 시 onSelect를 호출한다", async () => {
    const onSelect = vi.fn();
    render(<UserCard user={{ id: "1", name: "홍길동" }} onSelect={onSelect} />);
    await userEvent.click(screen.getByRole("button"));
    expect(onSelect).toHaveBeenCalledWith("1");
  });
});
```

## 실행

```bash
npx vitest run                           # 전체
npx vitest run src/features/auth/        # 슬라이스별
npx vitest run src/features/auth/ui/LoginForm.test.tsx  # 단건
```
