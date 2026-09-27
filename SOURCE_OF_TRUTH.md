# SOURCE OF TRUTH

This document defines the evidence hierarchy for **Latin America Digital Infrastructure**.

## Canonical hierarchy

1. Source-backed observations in `data/`.
2. `sources.csv` for the URL ledger of source-reference families used by the infrastructure sublayers.
3. `docs/methodology.md` and `docs/data_dictionary.md` for comparability and field definitions.
4. Validation scripts and GitHub Actions.
5. README, site and charts as presentation layers.

## Benchmark lineage

`sources.csv` is the canonical URL ledger. `data/metric_source_ledger.csv` maps every column in `data/regional_benchmark_2026.csv` to either an external source family, project metadata or a documented derived transformation.

This provides **metric-level provenance** for the harmonized benchmark. It is not equivalent to embedding a source URL in every individual cell. Detailed infrastructure tables retain their own row-level `source_ref` values where available.

The benchmark is a frozen vintage with `verified_cutoff=2026-08-13`. Live sources such as Internet Society Pulse can change later; those changes must not silently rewrite the historical benchmark.

## Integrity rules

- Preserve missing values rather than estimating them.
- Do not combine operational, under-construction, planned or announced infrastructure.
- Do not convert different infrastructure categories into a common total without a documented definition.
- Retain verification dates.
- Prefer primary provider, institutional or technical-registry evidence.
- Keep country and metro definitions explicit.

## Citation

Use `CITATION.cff` for the project and cite original source publishers for individual observations.
