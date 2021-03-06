# 3D e-Chem Virtual Machine

[![Build Status](https://travis-ci.org/3D-e-Chem/3D-e-Chem-VM.svg?branch=master)](https://travis-ci.org/3D-e-Chem/3D-e-Chem-VM)
[![DOI](https://zenodo.org/badge/19641/3D-e-Chem/3D-e-Chem-VM.svg)](https://zenodo.org/badge/latestdoi/19641/3D-e-Chem/3D-e-Chem-VM)

Scripts to create a Vagrant box using packer and ansible.

For available software/datasets/workflows inside Virtual machine see https://github.com/3D-e-Chem/3D-e-Chem-VM/wiki

# Usage

* VirtualBox, https://www.virtualbox.org
* Vagrant, https://www.vagrantup.com

Create a new directory and cd to it then start virtual machine with

```
vagrant init nlesc/3d-e-chem
vagrant up
```

Usage screencast on YouTube:

[![3D-e-Chem Virtual Machine screencast on YouTube](https://img.youtube.com/vi/zBv4rPfsLLc/0.jpg)](https://www.youtube.com/watch?v=zBv4rPfsLLc)

# Build

Requirements:

* Virtualbox, https://www.virtualbox.org/
* Packer, https://packer.io
* Enough disk space
  * Make sure temporary directory (/tmp by default on Linux) has enough space. Use TMPDIR environment variable to overwrite default location
* ova file `../Chemical-Analytics-Platform/output-virtualbox-iso/cap.ova` from build phase of https://github.com/NLeSC/Chemical-Analytics-Platform

```
packer build packer.json
```
# Test

Add box to Vagrant with

```
vagrant box remove --force --all nlesc/3d-e-chem
vagrant box add --name nlesc/3d-e-chem --force packer_virtualbox-ovf_virtualbox.box
```

Then use steps described at Usage chapter in a new directory.

# Push

Requirements:

* Vagrant cloud account, https://app.vagrantup.com/nlesc/boxes/3d-e-chem

Publish box on https://app.vagrantup.com/nlesc/boxes/3d-e-chem using the following steps:

1. Create a new version
2. Create a new provider
3. Choose `virtualbox` as provider
4. Choose Upload
5. Press `Continue to upload`
6. Upload the `packer_virtualbox-ivf_virtualbox.box` file generated by `vagrant package`
7. Edit version
8. Press `Release version`

# Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md).

# Cite

When using 3D-e-Chem-VM please cite one of the following:

* [Zenodo software release DOI](https://zenodo.org/badge/latestdoi/19641/3D-e-Chem/3D-e-Chem-VM)
* R. McGuire, S. Verhoeven, M. Vass, G. Vriend, I. J. P. De Esch, S. J. Lusher, R. Leurs, L. Ridder, A. J. Kooistra, T. Ritschel, C. de Graaf (2017). 3D-e-Chem-VM: Structural cheminformatics research infrastructure in a freely available Virtual Machine. Journal of Chemical Information and Modeling. doi: http://dx.doi.org/10.1021/acs.jcim.6b00686
