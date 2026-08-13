# Latin America Digital Infrastructure

Open, source-backed dataset and analytical framework for tracking digital infrastructure across Latin America.

**Español** — Repositorio abierto para mapear y comparar infraestructura digital en América Latina a partir de fuentes públicas y verificables.

## Scope

The project is designed as a reproducible regional observatory. It separates raw infrastructure observations from sources and analytical outputs so each record can be traced and updated.

The initial release focuses on hyperscale cloud infrastructure because provider documentation allows consistent verification across countries. Future modules are planned for:

- data centers and colocation facilities
- internet exchange points (IXPs)
- submarine cable systems and landing stations
- cloud regions and local/edge zones
- terrestrial backbone and fiber infrastructure
- international connectivity
- digital infrastructure policy and regulation

## Initial coverage

Version 0.1 includes a country reference table for 20 sovereign states commonly included in Latin America and a verified seed inventory of AWS, Google Cloud and Microsoft Azure infrastructure in Brazil, Chile, Mexico, Argentina and Peru.

The seed inventory is intentionally conservative. An infrastructure asset is included only when a primary provider source identifies the location or formally announces it.

## Repository structure

```text
latin-america-digital-infrastructure/
├── README.md
├── LICENSE
├── CITATION.cff
├── data/
│   ├── countries.csv
│   ├── hyperscaler_locations.csv
│   └── sources.csv
├── docs/
│   ├── methodology.md
│   └── data_dictionary.md
└── scripts/
    └── build_summary.py
```

## Data model

Each infrastructure observation records:

- country and city/location when publicly identified
- provider
- infrastructure type
- provider region or zone code
- operational status
- source identifier
- verification date
- notes needed to interpret the record

The source registry is kept separately in `data/sources.csv`.

## Seed dataset

The first release captures the following verified infrastructure types:

| Provider | Type | Countries represented |
|---|---|---|
| AWS | Cloud Region / Local Zone | Brazil, Mexico, Chile, Argentina, Peru |
| Google Cloud | Cloud Region | Brazil, Chile, Mexico |
| Microsoft Azure | Cloud Region | Brazil, Chile, Mexico |

AWS currently lists an operational region in Brazil, an operational region in Mexico and a future AWS Region in Chile. AWS also lists Local Zones in Buenos Aires, Lima and Santiago. Google Cloud documents regions in São Paulo, Santiago and Querétaro. Microsoft documents Azure regions in Brazil, Chile and Mexico.

## Reproducibility

Run:

```bash
python scripts/build_summary.py
```

The script reads `data/hyperscaler_locations.csv` and prints a country/provider summary without requiring external packages.

## Methodological principles

1. Prefer primary sources.
2. Store the source for every observation.
3. Distinguish operational, announced and restricted infrastructure.
4. Avoid treating edge locations, local zones, availability zones and full cloud regions as equivalent.
5. Record the verification date because infrastructure changes over time.
6. Do not infer undisclosed data-center capacity, investment or exact locations.

See `docs/methodology.md` for details.

## Roadmap

Planned next datasets:

- `data/ixps.csv`
- `data/submarine_cables.csv`
- `data/data_centers.csv`
- `data/cloud_edge.csv`
- `data/policy_regulation.csv`

Potential analytical outputs include country profiles, infrastructure concentration indicators, regional comparisons and geospatial visualizations.

## Sources

The initial source registry includes official documentation from AWS, Google Cloud and Microsoft Azure. PeeringDB is also registered as a future source for the IXP module.

All observations should be re-verified before being used in time-sensitive analysis.

## Author

Sebastian Elgueta Godoy

Sociology, public policy, telecommunications and digital infrastructure.

## License

Code is released under the MIT License. Source datasets remain subject to the terms of their original publishers. This repository does not claim ownership over third-party source data.
