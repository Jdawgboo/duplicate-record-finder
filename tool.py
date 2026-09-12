"""Detect exact duplicates in JSON-like records."""
from __future__ import annotations
import hashlib
import json
from collections import defaultdict
from typing import Any


def fingerprint(record: dict[str, Any]) -> str:
    encoded = json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(encoded.encode()).hexdigest()


def find_duplicates(records: list[dict[str, Any]]) -> dict[str, list[int]]:
    groups: dict[str, list[int]] = defaultdict(list)
    for index, record in enumerate(records): groups[fingerprint(record)].append(index)
    return {key: value for key, value in groups.items() if len(value) > 1}

if __name__ == "__main__":
    import sys
    print(json.dumps(find_duplicates(json.load(sys.stdin)), indent=2, sort_keys=True))
