# Latin America Digital Infrastructure

**Latest release:** [v0.2.0](https://github.com/selguetagodoy/latin-america-digital-infrastructure/releases/tag/v0.2.0) · [Concept DOI: 10.5281/zenodo.22921174](https://doi.org/10.5281/zenodo.22921174) · [Version DOI: 10.5281/zenodo.22921175](https://doi.org/10.5281/zenodo.22921175)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22921174.svg)](https://doi.org/10.5281/zenodo.22921174)

**Public dataset landing page:** https://selguetagodoy.github.io/dataset-latin-america-digital-infrastructure.html  
**Author profile:** https://selguetagodoy.github.io/

Public, source-backed observatory for comparing digital infrastructure across Latin America.

The current release covers eight benchmark markets — Argentina, Brazil, Chile, Colombia, Costa Rica, Mexico, Panama and Peru — and combines country indicators with separate datasets for cloud, Internet exchange, submarine connectivity and operator market presence.

## Regional snapshot

- 8 benchmark markets
- 27 comparable variables
- 16 active full cloud regions
- 92 active IXPs
- 1,045 MW of comparable operational data-center inventory across four harmonized markets

## Visual analysis

![Operational data center inventory](assets/market_scale.svg)

![Cloud regions and IXPs](assets/cloud_ixp_landscape.svg)

![Renewable generation and carbon intensity](assets/energy_profile.svg)

## Current release — v0.2

Start with:

- `PROJECT_OVERVIEW.md` — project scope and benchmark markets
- `data/regional_benchmark_2026.csv` — 27 comparable variables across eight countries
- `data/cloud_regions.csv` — AWS, Google Cloud, Microsoft Azure and Oracle Cloud Infrastructure
- `data/ixps.csv` — initial Internet exchange inventory
- `data/submarine_cables.csv` — selected regional submarine systems
- `data/operator_country_presence.csv` — public operator presence by country and market
- `docs/key_findings.md` — principal analytical findings
- `docs/country_profiles.md` — eight concise country profiles
- `docs/data_dictionary.md` — field definitions
- `docs/methodology.md` — evidence and comparability rules
- `site/` — static observatory website prepared for publication
- `CHANGELOG.md` — release history

## Public affairs data

### [Chile State Institutional Map](https://github.com/selguetagodoy/chile-state-institutional-map-)

Independent companion repository with a machine-readable institutional map of the Chilean State for **public affairs, public policy, regulatory analysis and stakeholder mapping**. The current release contains 849 institutional records with explicit source and coverage controls.

## Reproducibility

Run:

```bash
python scripts/benchmark_summary.py
python scripts/coverage_summary.py
```

GitHub Actions runs the same checks on pushes and pull requests.

## Research principles

The repository keeps infrastructure categories separate, uses harmonized comparisons only when definitions are sufficiently comparable, preserves missing values instead of estimating them, and distinguishes operational from announced infrastructure.

The public release is intentionally analytical rather than a directory of individual facilities.

## Author

**[Sebastián Elgueta Godoy](https://selguetagodoy.github.io/)** — sociologist and public affairs professional working on public policy, telecommunications, data centers, digital infrastructure, connectivity and comparative analysis in Latin America.

Profiles: [GitHub](https://github.com/selguetagodoy) · [LinkedIn](https://cl.linkedin.com/in/sebastian-elgueta-godoy) · [Substack](https://substack.com/@sebastianelguetagodoy) · [Coordenadas Públicas](https://www.coordenadaspublicas.cl/nosotros/)

## License

MIT for repository code. Third-party source data remain subject to the terms of their original publishers.
