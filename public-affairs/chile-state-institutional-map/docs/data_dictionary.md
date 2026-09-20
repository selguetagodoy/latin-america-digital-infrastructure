# Data dictionary

## institutional_map.csv

| Field | Definition |
|---|---|
| institution_id | Stable dataset identifier. |
| institution_name | Official or source-published institution name. |
| acronym | Acronym when explicitly modeled. |
| state_branch | Executive, Legislative, Judicial, autonomous or territorial layer. |
| institution_type | Institutional class used by this dataset. |
| parent_institution_id | Parent or sectoral institution when verified. |
| territorial_level | National, regional, provincial or communal. |
| region_code | Two-digit regional code where applicable. |
| region_name | Region name. |
| commune_code | Five-digit commune CUT code for municipalities. |
| commune_name | Commune name. |
| policy_area_primary | Primary policy domain for high-level stakeholder filtering. |
| legal_status | Structural/legal characterization when included. |
| source_id | Key to sources.csv. |
| verification_status | Evidence/coverage status. |
| last_verified | ISO verification date. |
| notes | Methodological or normalization note. |

## coverage_audit.csv

Controls whether a layer is complete against a known official universe. A blank official universe means that the project intentionally avoids claiming completeness until a stable denominator is established.

## Supplementary institutional tables

- `legislative_commissions.csv`: chamber, source order/number, stable ID, name, class, parent chamber, source and verification note.
- `state_universities.csv`: stable ID, official name, acronym, primary territorial reference, source and verification date.
- `state_cfts.csv`: stable ID, official name, region, main location, source and verification date.
- `public_enterprises_dipres.csv`: stable ID, source-published name, acronym, DIPRES directory provenance and verification date.
