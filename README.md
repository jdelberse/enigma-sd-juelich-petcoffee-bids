# Cologne "PetCoffee" Dataset (`juelich-petcoffee-bids`)

## Overview
**NB**: This dataset was shared and maintained under the name `juelich-petcoffee-bids`, which could not be changed. This dataset is one of two datasets (`juelich-petcoffee-bids` and `juelich-somnosafe-bids`) that make up the Cologne sample.

This dataset contains MRI data from a sleep manipulation study conducted at the German Aerospace Center (Germany). It is part of the ENIGMA-Sleep Working Group collection used to study the effects of sleep loss on glymphatic MRI indices. The data are organized according to the Brain Imaging Data Structure (BIDS) and managed with DataLad (git-annex).

## Sample

| Item | Value |
|---|---|
| Site | Cologne |
| Affiliation | German Aerospace Center |
| Country | Germany |
| Participants (N) | 48 |
| Age, mean (SD), years | 27.5 (4.9) |
| Male (%) | 60.4 |

## Sleep protocol

- **SD**: total sleep deprivation, 24 h
- **SR**: sleep restriction, 5 h TIB

Participants were scanned under baseline and sleep manipulation conditions.

## Imaging data

### T1-weighted (`anat/`)

| Parameter | Value |
|---|---|
| Scanner | Siemens Biograph mMR |
| Sequence | MPRAGE |
| TR (ms) | 2250 |
| TE (ms) | 3.03 |
| TI (ms) | 900 |
| Flip angle (°) | 9 |

## Data organization

- `sub-<ID>/ses-<label>/`: raw BIDS data (`anat/`)
- `participants.tsv`: participant-level information
- `sub-<ID>/sub-<ID>_sessions.tsv`: session-level information (condition, visit, date, time)
- `derivatives/`: processed outputs, if present

File contents are tracked with git-annex. After cloning, retrieve data with `datalad get <path>`.

## Original publication

Lin, Y.-S., Lange, D., Baur, D. M., Foerges, A., Chu, C., Li, C., Elmenhorst, E.-M., Neumaier, B., Bauer, A., Aeschbach, D., Landolt, H.-P., & Elmenhorst, D. (2024). Repeated caffeine intake suppresses cerebral grey matter responses to chronic sleep restriction in an A1 adenosine receptor-dependent manner: a double-blind randomized controlled study with PET-MRI. *Scientific Reports*, 14, 12724. [https://doi.org/10.1038/s41598-024-61421-8](https://doi.org/10.1038/s41598-024-61421-8)

## Contact

- Jorik D. Elberse: [j.elberse@fz-juelich.de](mailto:j.elberse@fz-juelich.de)
- Masoud Tahmasian: [m.tahmasian@fz-juelich.de](mailto:m.tahmasian@fz-juelich.de)
