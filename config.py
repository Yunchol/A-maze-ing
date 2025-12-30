# config.py
from typing import Dict


def load_config(path: str) -> Dict[str, str]:
    config: Dict[str, str] = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # 空行・コメント行は無視
            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(f"Invalid config line: {line}")

            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

    return config
