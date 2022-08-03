#!/bin/sh

if [[ -z $1  ]]; then
	echo "-------------------------------------"
	echo "Usage: <package-name> <architecture>"
	echo "-------------------------------------"
	echo "You must specify a package name and an architecture."
	echo "Achitecture options are \"32\" for 32 bit and \"64\" for 64 bit"
	echo "-------------------------------------"
	echo "64 bit package names are:"
	ls x86_64/ | sed 's/ /\n/g'
	echo "-------------------------------------"
	echo "32 bit package names are:"
	ls i686/ | sed 's/.i686//g'
	exit 1
fi

# install some build dependencies
sudo dnf -y install mock pykickstart fedpkg libvirt

# add current user to 'mock' build group
sudo usermod -a -G mock $USER

# turn selinux off if it's enabled
sudo setenforce 0

# make a destination folder for our packages
mkdir -p packages

# enter the repository of the package to build:
if [[ "$2" == "32" ]]; then
	BUILDARCH="i386"
	cd i686/$1.i686
else
	BUILDARCH="x86_64"
	cd x86_64/$1
fi

# create a fedora srpm from the spec sheet
fedpkg --release f36 srpm

# build the package
mock -r /etc/mock/fedora-36-$BUILDARCH.cfg --enable-network --rebuild *.src.rpm

# cleanup our source rpm
rm *.src.rpm

# move the package to our main folder
cd ../../
if [[ "$BUILDARCH" == "i386" ]]; then
	sudo mv /var/lib/mock/fedora-36-i686/result/*.rpm packages/
else
	sudo mv /var/lib/mock/fedora-36-$BUILDARCH/result/*.rpm packages/
fi

# cleanup our source rpm (again)
rm packages/*.src.rpm

# re-enable selinux if needed
sudo setenforce 1

# cleanup
mock -r /etc/mock/fedora-36-x86_64.cfg --scrub=all
mock -r /etc/mock/fedora-36-i386.cfg --scrub=all

