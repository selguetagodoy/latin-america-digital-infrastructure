# Chile State Institutional Map

**Open institutional map of the Chilean State for public affairs, public policy, regulatory analysis and stakeholder mapping.**

Part of the [Latin America Digital Infrastructure](../../README.md) research ecosystem by Sebastián Elgueta Godoy.

## What this release contains

This first structural release builds a machine-readable institutional spine of the Chilean State, separating stable institutions from volatile officeholders.

- **25 ministries**
- **162 public services/repartitions exactly as published by Gob.cl**
- **40 subsecretariats in the initial structural layer**
- **16 Regional Governments (GORE)**
- **16 Presidential Regional Delegations (DPR)**
- **40 Presidential Provincial Delegations (DPP)**
- **345 municipalities**
- top-level Legislative, Judicial and constitutionally autonomous bodies
- a **2026 supplement layer** for institutions that require current control beyond the general directory, including ANCI, SERMIG, SBAP and CMF

The master table currently contains **660 records**.

## Why two layers are used

A public-affairs dataset cannot treat an official directory as automatically synonymous with a fully normalized current institutional structure. The Gob.cl directory reports 162 public services, but some labels can preserve legacy nomenclature or lag recent institutional reforms. For that reason:

1. `executive_public_services_gobcl.csv` preserves the official directory **literally and reproducibly**.
2. `institutional_map.csv` adds structural layers and explicitly flagged current supplements.
3. `coverage_audit.csv` shows what is complete, what is complete only "as published", and what remains a controlled expansion layer.

This avoids silently replacing, merging or reclassifying institutions.

## Files

- `data/institutional_map.csv` — master institutional table
- `data/executive_public_services_gobcl.csv` — complete 162-record Gob.cl public-service directory snapshot
- `data/ministries.csv` — 25 ministries
- `data/municipalities.csv` — 345 municipalities
- `data/institutional_relations.csv` — parent/sectoral and territorial relationships
- `data/coverage_audit.csv` — coverage control against official universes
- `sources.csv` — source register
- `docs/data_dictionary.md` — field definitions
- `docs/methodology.md` — inclusion, verification and normalization rules
- `scripts/validate.py` — reproducibility checks

## Scope

"State institutional map" means **institutional units**, not every physical establishment. A hospital, police station, school, courthouse or regional office is not automatically a separate institution in this dataset. Those operational establishments can be added later as linked child datasets without changing stable institutional IDs.

## Public-affairs use cases

The model is designed to support:

- stakeholder mapping
- institutional and regulatory intelligence
- public consultation tracking
- permitting maps
- legislative/regulatory monitoring
- public-sector procurement intelligence
- cross-country LATAM comparisons

## Verification date

**2026-09-19**

## Author

**Sebastián Elgueta Godoy** — Sociologist · Public Affairs · Public Policy · Digital Infrastructure · Latin America.

The dataset prioritizes primary and official sources and keeps provenance and uncertainty explicit.
