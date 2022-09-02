%undefine _auto_set_build_flags
%global amdpro 22.20.3
%global major 22.20
%global minor 1462318
%global amf 1.4.26
%global enc 1.0
%global rhel_major 9.0
%global rhel_minor 9
%global amdvlk 2022.Q3.3
%global fedora fc36
%global ubuntu 22.04

Name:     libdrm-pro
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD proprietary libdrm
URL:      http://repo.radeon.com/amdgpu

Provides:      libdrm-pro
Provides:      libdrm-pro(i686)
Provides:      libdro.so.2()
Provides:      libdro_amdgpu.so.1()
Provides:      libdro_radeon.so.1()
Provides:      libdro.so.2()(i686)
Provides:      libdro_amdgpu.so.1()(i686)
Provides:      libdro_radeon.so.1()(i686)
Provides:      libdro.so.2()(x86_32)
Provides:      libdro_amdgpu.so.1()(x86_32)
Provides:      libdro_radeon.so.1()(x86_32)
Provides:      libdro.so.2()(32bit)
Provides:      libdro_amdgpu.so.1()(32bit)
Provides:      libdro_radeon.so.1()(32bit)

Requires: 	libdrm-pro(x86_64)
Requires: 	libdrm

BuildRequires: wget 
BuildRequires: cpio

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget -r -nd --no-parent -A 'libdrm-amdgpu-amdgpu1*%{ubuntu}_i386.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

wget -r -nd --no-parent -A 'libdrm-amdgpu-radeon1*%{ubuntu}_i386.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

wget -r -nd --no-parent -A 'libdrm2-amdgpu*%{ubuntu}_i386.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

#

ar -x ../libdrm-amdgpu-amdgpu1*%{ubuntu}_i386.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

#

ar -x ../libdrm-amdgpu-radeon1*%{ubuntu}_i386.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

#

ar -x ../libdrm2-amdgpu*%{ubuntu}_i386.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

###

#

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu/libdrm/lib32

mv ./opt/amdgpu/lib/i386-linux-gnu/libdrm.so.2.4.0 ./opt/amdgpu/libdrm/lib32/libdro.so.2.4.0

mv ./opt/amdgpu/lib/i386-linux-gnu/libdrm_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib32/libdro_amdgpu.so.1.0.0

mv ./opt/amdgpu/lib/i386-linux-gnu/libdrm_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib32/libdro_radeon.so.1.0.1

#

ln -s /opt/amdgpu/libdrm/lib32/libdro.so.2.4.0 ./opt/amdgpu/libdrm/lib32/libdro.so.2

ln -s /opt/amdgpu/libdrm/lib32/libdro_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib32/libdro_amdgpu.so.1

ln -s /opt/amdgpu/libdrm/lib32/libdro_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib32/libdro_radeon.so.1

#

ln -s /opt/amdgpu/libdrm/lib32/libdro.so.2.4.0 ./opt/amdgpu/libdrm/lib32/libdro.so

ln -s /opt/amdgpu/libdrm/lib32/libdro_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib32/libdro_amdgpu.so

ln -s /opt/amdgpu/libdrm/lib32/libdro_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib32/libdro_radeon.so

# 

rm -r ./usr/share

# 

echo "adding needed library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/libdrm-pro-i686.conf

echo "/opt/amdgpu/libdrm/lib32" > ./etc/ld.so.conf.d/libdrm-pro-i686.conf

mkdir -p ./etc/profile.d

touch ./etc/profile.d/libdrm-pro-i686.sh

echo 'export LD_LIBRARY_PATH="/opt/amdgpu/libdrm/lib32:$LD_LIBRARY_PATH"' > ./etc/profile.d/libdrm-pro-i686.sh

cd %{buildroot}/debs/extract

mv opt %{buildroot}/
mv etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'

%description
AMD proprietary libdrm

%files
"/opt/amdgpu/libdrm/lib32/*.so*"
"/etc/ld.so.conf.d/libdrm-pro-i686.conf"
"/etc/profile.d/libdrm-pro-i686.sh"
%exclude "/debs"
%exclude "/opt/amdgpu/lib/i386-linux-gnu"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
