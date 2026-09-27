#!/usr/bin/env python3
"""Reproduce and validate the physical RTT proxy used by the regional benchmark."""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "regional_benchmark_2026.csv"

EARTH_RADIUS_KM = 6371.0
FIBER_PROPAGATION_KM_S = 200_000.0
ROUTE_FACTOR = 1.3

COORDS = {
    "Bogotá": (4.7110, -74.0721),
    "São Paulo": (-23.5505, -46.6333),
    "Querétaro": (20.5888, -100.3899),
    "Santiago": (-33.4489, -70.6693),
    "Lima": (-12.0464, -77.0428),
    "Ciudad de Panamá": (8.9824, -79.5199),
    "San José": (9.9281, -84.0907),
    "Buenos Aires": (-34.6037, -58.3816),
    "Miami": (25.7617, -80.1918),
}


def haversine_km(a: tuple[float, float], b: tuple[float, float]) -> float:
    lat1, lon1 = map(math.radians, a)
    lat2, lon2 = map(math.radians, b)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return EARTH_RADIUS_KM * 2 * math.asin(math.sqrt(h))


def physical_rtt_ms(origin: str, destination: str) -> float:
    distance = haversine_km(COORDS[origin], COORDS[destination])
    seconds = distance * ROUTE_FACTOR * 2 / FIBER_PROPAGATION_KM_S
    return round(seconds * 1000, 2)


def main() -> int:
    failures: list[str] = []
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    for row in rows:
        market = row["anchor_market"]
        expected_miami = physical_rtt_ms(market, "Miami")
        expected_sp = physical_rtt_ms(market, "São Paulo")
        actual_miami = float(row["rtt_physical_miami_ms"])
        actual_sp = float(row["rtt_physical_sao_paulo_ms"])

        if actual_miami != expected_miami:
            failures.append(f"{market}: Miami {actual_miami} != {expected_miami}")
        if actual_sp != expected_sp:
            failures.append(f"{market}: São Paulo {actual_sp} != {expected_sp}")

    print(
        f"Physical RTT check: {len(rows)} markets · route_factor={ROUTE_FACTOR} · "
        f"fiber_speed={FIBER_PROPAGATION_KM_S:.0f} km/s"
    )
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1
    print("OK: all benchmark RTT proxy values reproduce exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
