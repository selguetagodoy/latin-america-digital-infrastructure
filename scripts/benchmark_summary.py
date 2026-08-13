#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "regional_benchmark_2026.csv"

NUMERIC_METRICS = [
    "dc_inventory_operational_mw",
    "dc_vacancy_pct",
    "cloud_regions_active",
    "ixps_active",
    "internet_resilience_index",
    "renewable_generation_pct",
    "carbon_intensity_gco2e_kwh",
    "corporate_income_tax_pct",
    "wjp_rule_of_law_score",
    "nri_total_2025",
]

with DATA.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

print(f"Markets: {len(rows)}")
print(f"Variables: {len(rows[0]) if rows else 0}")
print()

for metric in NUMERIC_METRICS:
    observed = []
    for row in rows:
        raw = row.get(metric, "").strip()
        if not raw:
            continue
        try:
            observed.append((float(raw), row["country"]))
        except ValueError:
            pass
    observed.sort(reverse=True)
    print(metric)
    if not observed:
        print("  no observations")
        continue
    for value, country in observed:
        print(f"  {country}: {value:g}")
    print()

missing = []
for row in rows:
    blanks = sum(1 for value in row.values() if value is None or not str(value).strip())
    missing.append((blanks, row["country"]))

print("Missing fields by country")
for blanks, country in sorted(missing):
    print(f"  {country}: {blanks}")
