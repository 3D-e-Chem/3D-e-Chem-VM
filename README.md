Scripts to create a Vagrant box using packer and ansible.

# Usage

* VirtualBox, https://www.virtualbox.org
* Vagrant, https://www.vagrantup.com

Start virtual machine with

```
vagrant init NLeSC/3D-e-Chem-VM
vagrant up
```

# Build

Requirements:

* Virtualbox, https://www.virtualbox.org/
* Vagrant, https://www.vagrantup.com/
* Packer, https://packer.io
* Atlas account, https://atlas.hashicorp.com
* Enough disk space
  * Make sure temporary directory (/tmp by default on Linux) has enough space. Use TMPDIR environment variable to overwrite default location

```
packer build packer.json
```
# Test

Add box to Vagrant with

```
vagrant box add --name NLeSC/3D-e-Chem --box-version <version> packer_virtualbox-iso_virtualbox.box
```
Where `<version>` is higher than box on https://atlas.hashicorp.com.

Then use steps described at Usage chapter.
