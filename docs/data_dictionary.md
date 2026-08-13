# Data dictionary

## `data/countries.csv`

Country reference table using ISO3 codes and a working Latin American subregion classification.

## `data/regional_benchmark_2026.csv`

Eight-country comparative table. It combines market, connectivity, cloud, energy and institutional indicators. Blank cells mean that a sufficiently comparable public observation was not retained.

Key field groups:

- identity — `country`, `iso3`, `anchor_market`, `benchmark_role`
- market scale — `dc_inventory_operational_mw`, `dc_vacancy_pct`, `dc_absorption_net_mw`, rent-band fields
- cloud — `cloud_regions_active`, `cloud_regions_announced`
- interconnection — `ixps_active`, `ixp_members`, domestic-network participation, cache and resilience fields
- energy — business electricity price, renewable share, carbon intensity and standard connection proxy
- institutions — corporate tax, WJP, NRI and ITU cybersecurity tier
- geography — physical-distance latency proxies to Miami and São Paulo
- versioning — `verified_cutoff`

## `data/cloud_regions.csv`

Provider-defined full cloud regions from AWS, Google Cloud, Microsoft Azure and Oracle Cloud Infrastructure. Status is kept separate so operational, announced and restricted regions are not counted as equivalent.

## `data/ixps.csv`

Initial exchange-level inventory. IXP counts used in the regional benchmark are maintained as a separate harmonized country indicator.

## `data/submarine_cables.csv`

Selected submarine cable systems relevant to Latin American connectivity. Cable systems are not treated as data centers or cloud regions.

## `data/operator_country_presence.csv`

Publicly documented operator presence by country and market. This file is deliberately market-level and is not intended to be a facility directory.

Last updated: 2026-08-13.
