#!/usr/bin/env python3
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "countries.csv"

with DATA.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

print(f"Countries in reference table: {len(rows)}")
print("\nBy subregion")
for subregion, count in sorted(Counter(r["subregion"] for r in rows).items()):
    print(f"  {subregion}: {count}")
