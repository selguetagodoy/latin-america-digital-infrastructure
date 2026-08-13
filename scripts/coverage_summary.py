#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

FILES = {
    "countries": "countries.csv",
    "regional_benchmark_2026": "regional_benchmark_2026.csv",
    "cloud_regions": "cloud_regions.csv",
    "ixps": "ixps.csv",
    "submarine_cables": "submarine_cables.csv",
    "operator_country_presence": "operator_country_presence.csv",
}

for label, filename in FILES.items():
    path = DATA / filename
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    print(f"{label}: {len(rows)} records")
