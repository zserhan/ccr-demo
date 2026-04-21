"""Utility helpers."""
import json
from pathlib import Path


def load_config(path: str) -> dict:
    """Load a JSON config file."""
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)
