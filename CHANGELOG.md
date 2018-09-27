# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).
Formatted as described on http://keepachangelog.com/.

## [Unreleased]

## [1.4.4] - 2018-09-27

Based on [Chemical Analytics Platform](https://github.com/NLeSC/Chemical-Analytics-Platform) version 0.8.6

## [1.4.3] - 2018-02-09

### Changed

* 3D-e-Chem node collection v1.1.3
* Upgraded Virtualbox Guest Additions to v5.2.6
* Upgrade KNIME to v3.5.2
* Upgraded RDKit to 2017_09_3

### Fixed

- Made Python version 2 the default in KNIME

## [1.4.2] - 2017-12-06

### Changed

- adapted to new format of workflows repo

## [1.4.1] - 2017-11-12

Based on [Chemical Analytics Platform](https://github.com/NLeSC/Chemical-Analytics-Platform) version 0.8.5

### Added

- PLANTS example workflow
- Silicos-IT example workflows

### Changed

- Upgraded KripoDB to v2.3.1

## [1.4.0] - 2017-03-10

Based on [Chemical Analytics Platform](https://github.com/NLeSC/Chemical-Analytics-Platform) version 0.8.4

### Changed

- Upgraded KripoDB to v2.2.1

## Removed

- KripoDB PDB dataset, use web service to get latest dataset

## [1.3.0] - 2017-01-26

### Added

- KNIME molviewer example workflow (#27)

### Changed

- Switched to single 3D-e-Chem feature instead of every node separately (#28)
- Upgraded KNIME to v3.3.1
- Upgraded KripoDB to v2.1.0

## [1.2.0] - 2016-09-04

Based on [Chemical Analytics Platform](https://github.com/NLeSC/Chemical-Analytics-Platform) version 0.8.2

### Added

- Sygma Python library and KNIME node (#20)

### Changed

- Disabled Virtualbox 3D accleration, so webgl works
- 3D-e-Chem workflows from single GitHub repo (#21)
- Kripo fragments db source url (#22)
- Upgraded Knime to v3.2.1

### Fixed

- Kripodb sample data set renamed (#19)

## [1.1.1] - 2016-06-08

### Fixed

- Modified tanimoto node install fails (#17)

### Added

- Chemdb4VS workflow
- Klifs Knime nodes & example workflow (#14)
- Kripo fragments db for whole PDB
- Kripo bioisosteric replacement workflow (#16)
- Pymol sessions for Kripo and GPCRDB published (#18)

### Changed

- Updated KripoDB to 1.4.2
- Workflow examples are always downloaded to force latest version.

## [1.1.0] - 2016-05-07

### Changed

- Based on Chemical Analytics Platform 0.8.0
- Upgraded RDKit to 2016.03.1
- Upgraded Ubuntu to 16.04
- Upgraded Knime to v3.1.2
- Upgraded Virtualbox Guest Additions to v5.0.20

### Added

- ss-TEA Knime node

## [1.0.3] - 2016-05-03

### Added

- Kripodb GPCR sample dataset (#12)

### Changed

- Updated Knime to 3.1.2
- Updated Ubuntu to 14.04.4
- Updated KripoDB to 1.4.0

## [1.0.2] - 2016-01-23

### Fixed

- Allow vagrant user to update Knime
- self upgrade script gets overwritten by cap (#6)

## [1.0.1] - 2016-01-22

### Changed

- Based on Chemical Analytics Platform (https://github.com/NLeSC/Chemical-Analytics-Platform)

### Added

- 3D e Chem software, Knime nodes, Fingerprint cli

## [1.0.0] - 2016-01-16

Initial release with Knime, rdkit, postgresql, R and lxde.

### Added

- RDKit (#2)
- Postgresql (#1)
- Chembl postgresql script (#3)
