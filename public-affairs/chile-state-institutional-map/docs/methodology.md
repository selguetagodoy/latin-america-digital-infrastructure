# Methodology

## Unit of analysis

One row represents an institutional unit. Physical establishments and local offices are excluded unless they have a distinct institutional/legal identity.

## Source hierarchy

1. Primary official institutional source.
2. Gob.cl institutional directory.
3. BCN/LeyChile organic legislation.
4. SUBDERE/SINIM territorial sources.
5. Government Digital and sectoral official registries for cross-checking.

## Preservation rule

The 162-item Gob.cl services layer is preserved exactly as published on 2026-09-19. It is not silently "corrected". When a current institution is demonstrably missing from, newer than, or renamed relative to the general directory, it is added as a separately flagged supplement.

This is intentional. Public-affairs analysis needs both:
- the official source snapshot; and
- the normalized/current analytical layer.

## Territorial rules

Chile has 346 communes but 345 municipalities. Antártica is the exception: it has no municipality of its own and is administered in the municipal grouping with Cabo de Hornos. The municipal table therefore contains 345 institutional rows. Municipality names and CUT codes in v0.1 use the normalized open-data catalogue from `cortega26/chile-hub` as a structured seed; the official national universe of 345 municipalities and the Antártica exception are cross-checked against SUBDERE. This provenance is recorded explicitly rather than attributing the row-level extraction directly to SUBDERE.

The regional layer contains 16 GOREs and 16 DPRs. The provincial executive layer contains 40 DPPs because, in the province that is the seat of each regional capital, the DPR exercises the provincial functions.

## IDs

Stable IDs are dataset identifiers, not official government codes unless explicitly stated.

- `CL-MIN-*` ministries
- `CL-SUB-*` subsecretariats
- `CL-SP-###` Gob.cl directory services, preserving source order
- `CL-GORE-##`
- `CL-DPR-##`
- `CL-DPP-###`
- `CL-MUN-#####` municipality using commune CUT code
- `CL-SUP-*` current verified supplements

## Verification statuses

- `official_directory_complete` — complete against a stated official directory universe.
- `official_directory_as_published` — source is preserved literally; normalization may still be required.
- `territorial_catalogue_complete` — complete against the territorial universe.
- `current_official_supplement` — current institution verified outside the general directory.
- `ministerial_structure_v0_1` — structural layer included and subject to periodic revalidation.
- `core_top_level` — superior body included; operational substructure may be modeled separately.

## Known normalization issues

The general official directory can contain legacy or non-current naming. Examples are not overwritten in the literal source layer. Instead, current counterparts are added or reconciled through supplements and future crosswalk tables.

## Next controlled expansions

The schema is ready for:
- permanent commissions of both chambers
- courts of appeals and special tribunals
- State universities
- public enterprises and SEP companies
- SLEPs and other decentralized education bodies
- sectoral/regional offices
- officeholder history with valid-from / valid-to dates
- competencies, regulatory powers, permitting powers and consultation mechanisms backed by organic law.

## Legislative commission rule

For the Chamber, the dataset follows the live operational commission page as verified on 2026-09-19. That page lists 34 commission/subcommission entries. The institutional FAQ still states 27 permanent commissions, so the discrepancy is preserved as a source note rather than silently reconciled.

For the Senate, the master includes the 24 bodies identified by the Senate as permanent legislative commissions. Internal commissions (Régimen Interior, Revisora de Cuentas, Ética y Transparencia) and the Comisión Especial Mixta de Presupuestos are not counted inside that 24-row legislative subset.

## State higher education

The dataset includes the complete current universes of 18 State universities and 15 State Technical Training Centers. Universities are modeled as autonomous State institutions and are not assigned a hierarchical parent ministry. Sectoral relations to the Ministry of Education are represented separately in the relationship table.

## Public enterprises

The public-enterprise layer uses the current DIPRES Empresas Públicas directory as the operational universe and preserves its names as published. This layer is explicitly distinguished from the SEP portfolio because the two systems have different coverage purposes.

## Public Education Local Services (SLEP)

The dataset includes the full statutory universe of 70 Servicios Locales de Educación Pública established under Law N°21.040. They are modeled as functionally and territorially decentralized public bodies with legal personality and their own assets. Their relationship to the Ministry of Education is represented through the Dirección de Educación Pública. Implementation/transfer status is deliberately kept separate from institutional existence because the rollout changes over time.
