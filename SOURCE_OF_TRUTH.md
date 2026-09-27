# SOURCE OF TRUTH

This document defines the evidence hierarchy for **Latin America Digital Infrastructure**.

## Canonical hierarchy

1. Source-backed observations in `data/`.
2. `sources.csv` for the URL ledger of source-reference families used by the infrastructure sublayers.
3. `docs/methodology.md` and `docs/data_dictionary.md` for comparability and field definitions.
4. Validation scripts and GitHub Actions.
5. README, site and charts as presentation layers.

## Important lineage boundary

The current `sources.csv` maps the explicit `source_ref` families used in cloud, IXP, submarine-cable and operator-presence tables. The harmonized `data/regional_benchmark_2026.csv` contains a broader 27-variable comparison and **does not yet provide row-by-row URL lineage for every metric**. It must not be described as having complete source-level provenance until that ledger is added.

## Integrity rules

- Preserve missing values rather than estimating them.
- Do not combine operational, under-construction, planned or announced infrastructure.
- Do not convert different infrastructure categories into a common total without a documented definition.
- Retain verification dates.
- Prefer primary provider, institutional or technical-registry evidence.
- Keep country and metro definitions explicit.

## Citation

Use `CITATION.cff` for the project and cite original source publishers for individual observations.
