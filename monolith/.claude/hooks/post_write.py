#!/usr/bin/env python3
"""PostToolUse hook: Write/Edit 완료 후 파일 타입에 따라 포맷터/린터 실행."""

import json
import subprocess
import sys
from pathlib import Path


def main():
    try:
        data = json.loads(sys.stdin.read())
        file_path = data.get("tool_input", {}).get("file_path", "") or data.get(
            "tool_response", {}
        ).get("filePath", "")
    except (json.JSONDecodeError, KeyError):
        return

    if not file_path or not Path(file_path).exists():
        return

    # Python → ruff format
    if file_path.endswith(".py"):
        subprocess.run(
            ["ruff", "format", "--quiet", file_path],
            capture_output=True,
            timeout=15,
        )

    # TypeScript/JavaScript → eslint --fix
    elif file_path.endswith((".ts", ".tsx", ".js", ".jsx")):
        frontend_dir = Path(file_path)
        while frontend_dir.name != "frontend" and frontend_dir != frontend_dir.parent:
            frontend_dir = frontend_dir.parent
        if frontend_dir.name == "frontend":
            subprocess.run(
                ["npx", "eslint", "--fix", file_path],
                cwd=str(frontend_dir),
                capture_output=True,
                timeout=30,
            )


if __name__ == "__main__":
    main()
