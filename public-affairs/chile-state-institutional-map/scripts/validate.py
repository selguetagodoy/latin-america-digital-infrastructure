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
commissions = read("legislative_commissions.csv")
universities = read("state_universities.csv")
cfts = read("state_cfts.csv")
enterprises = read("public_enterprises_dipres.csv")
master = read("institutional_map.csv")

assert len(ministries) == 25, len(ministries)
assert len(services) == 162, len(services)
assert len(municipalities) == 345, len(municipalities)
assert len(commissions) == 58, len(commissions)
assert sum(r["chamber"] == "Cámara de Diputadas y Diputados" for r in commissions) == 34
assert sum(r["chamber"] == "Senado" for r in commissions) == 24
assert len(universities) == 18, len(universities)
assert len(cfts) == 15, len(cfts)
assert len(enterprises) == 28, len(enterprises)
assert len(master) == 779, len(master)
assert len({r["institution_id"] for r in master}) == len(master), "Duplicate institution_id"
assert len({r["commune_code"] for r in municipalities}) == 345, "Duplicate commune code"
assert "12202" not in {r["commune_code"] for r in municipalities}, "Antártica must not be represented as a municipality"

print({
    "ministries": len(ministries),
    "gobcl_public_services": len(services),
    "municipalities": len(municipalities),
    "legislative_commissions": len(commissions),
    "state_universities": len(universities),
    "state_cfts": len(cfts),
    "public_enterprises_dipres": len(enterprises),
    "master_records": len(master),
    "status": "OK"
})
