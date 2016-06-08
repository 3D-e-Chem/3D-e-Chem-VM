# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Fixed

* Modified tanimoto node install fails (#17)

### Added

* Chemdb4VS workflow
* Klifs Knime nodes & example workflow (#14)
* Kripo fragments db for whole PDB
* Kripo bioisosteric replacement workflow (#16)
* Pymol sessions for Kripo and GPCRDB published (#18)

### Changed

* Updated KripoDB to 1.4.2
* Workflow examples are always downloaded to force latest version.

## [1.1.0] - 2016-05-07

### Changed

* Based on Chemical Analytics Platform 0.8.0
* Upgraded RDKit to 2016.03.1
* Upgraded Ubuntu to 16.04
* Upgraded Knime to v3.1.2
* Upgraded Virtualbox Guest Additions to v5.0.20

### Added

* ss-TEA Knime node

## [1.0.3] - 2016-05-03

### Added

* Kripodb GPCR sample dataset (#12)

### Changed

* Updated Knime to 3.1.2
* Updated Ubuntu to 14.04.4
* Updated KripoDB to 1.4.0

## [1.0.2] - 2016-01-23

### Fixed

* Allow vagrant user to update Knime
* self upgrade script gets overwritten by cap (#6)

## [1.0.1] - 2016-01-22

### Changed

* Based on Chemical Analytics Platform (https://github.com/NLeSC/Chemical-Analytics-Platform)

### Added

* 3D e Chem software, Knime nodes, Fingerprint cli

## [1.0.0] - 2016-01-16

Initial release with Knime, rdkit, postgresql, R and lxde.

### Added

* RDKit (#2)
* Postgresql (#1)
* Chembl postgresql script (#3)
