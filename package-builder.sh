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
sudo dnf -y install wget cpio mock pykickstart fedpkg libvirt fedora-packager rpmdevtools

# turn selinux off if it's enabled
sudo setenforce 0

# make a destination folder for our packages
mkdir -p packages

# Setup tree
mkdir -p SOURCES
mkdir -p SPECS
mkdir -p SRPMS
mkdir -p BUILD
mkdir -p BUILDROOT

# enter the repository of the package to build:
if [[ "$2" == "32" ]]; then
	export BUILDARCH="i686"
	cd i686/$1.i686
else
	export BUILDARCH="x86_64"
	cd x86_64/$1
fi



# build the package
rpmbuild -bb --define "_srcrpmdir $(pwd)/../../packages " --undefine=_disable_source_fetch  --target="$BUILDARCH" *.spec --define "_topdir $(pwd)/../.." --define "_rpmdir $(pwd)/../../packages"


# enter main dir

cd ../../

# Clean
rm -r BUILD
rm -r BUILDROOT

# Move rpms to packages

mv packages/x86_64/* packages/ || echo 'not a 64 bit package , this is ok!'

mv packages/i686/* packages/ || echo 'not a 32 bit package , this is ok!'


# re-enable selinux if needed
sudo setenforce 1

