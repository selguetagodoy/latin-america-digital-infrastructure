import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def read(name):
    with open(DATA / name, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

ministries = read("ministries.csv")
services = read("executive_public_services_gobcl.csv")
municipalities = read("municipalities.csv")
master = read("institutional_map.csv")

assert len(ministries) == 25, len(ministries)
assert len(services) == 162, len(services)
assert len(municipalities) == 345, len(municipalities)
assert len({r["institution_id"] for r in master}) == len(master), "Duplicate institution_id"
assert len({r["commune_code"] for r in municipalities}) == 345, "Duplicate commune code"
assert "12202" not in {r["commune_code"] for r in municipalities}, "Antártica must not be represented as a municipality"

print({
    "ministries": len(ministries),
    "gobcl_public_services": len(services),
    "municipalities": len(municipalities),
    "master_records": len(master),
    "status": "OK"
})
