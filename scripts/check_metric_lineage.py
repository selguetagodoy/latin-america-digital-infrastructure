#!/usr/bin/env python3
"""Ensure every regional benchmark column has documented metric lineage."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "data" / "regional_benchmark_2026.csv"
LEDGER = ROOT / "data" / "metric_source_ledger.csv"
SOURCES = ROOT / "sources.csv"


def main() -> int:
    with BENCHMARK.open(encoding="utf-8-sig", newline="") as fh:
        header = next(csv.reader(fh))

    with LEDGER.open(encoding="utf-8-sig", newline="") as fh:
        ledger = list(csv.DictReader(fh))

    with SOURCES.open(encoding="utf-8-sig", newline="") as fh:
        source_ids = {row["source_id"].strip() for row in csv.DictReader(fh)}

    mapped: dict[str, str] = {}
    failures: list[str] = []

    for row in ledger:
        fields = [x.strip() for x in row["metric_fields"].split("|") if x.strip()]
        ids = [x.strip() for x in row["source_ids"].split("|") if x.strip()]
        for field in fields:
            if field in mapped:
                failures.append(f"duplicate mapping for {field}")
            mapped[field] = row["source_ids"]
        for source_id in ids:
            if source_id in {"project_metadata"}:
                continue
            if source_id not in source_ids:
                failures.append(f"unknown source_id {source_id} in ledger")

    missing = [field for field in header if field not in mapped]
    extra = [field for field in mapped if field not in header]
    if missing:
        failures.append("unmapped benchmark fields: " + ", ".join(missing))
    if extra:
        failures.append("ledger fields absent from benchmark: " + ", ".join(extra))

    print(f"Metric lineage check: {len(header)} benchmark columns · {len(mapped)} mapped.")
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1
    print("OK: every benchmark column has documented lineage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
