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
Provides:      libdrm-pro(x86_64)

Provides:      libdrm.so.2()
Provides:      libdrm_amdgpu.so.1()
Provides:      libdrm_radeon.so.1()
Provides:      libdrm.so.2()(x86_64)
Provides:      libdrm_amdgpu.so.1()(x86_64)
Provides:      libdrm_radeon.so.1()(x86_64)
Provides:      libdrm.so.2()(64bit)
Provides:      libdrm_amdgpu.so.1()(64bit)
Provides:      libdrm_radeon.so.1()(64bit)

Requires: 	libdrm

BuildRequires: wget 
BuildRequires: cpio

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget -r -nd --no-parent -A 'libdrm-amdgpu-amdgpu1*%{ubuntu}_amd64.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

wget -r -nd --no-parent -A 'libdrm-amdgpu-radeon1*%{ubuntu}_amd64.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

wget -r -nd --no-parent -A 'libdrm2-amdgpu*%{ubuntu}_amd64.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

#

ar -x ../libdrm-amdgpu-amdgpu1*%{ubuntu}_amd64.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

#

ar -x ../libdrm-amdgpu-radeon1*%{ubuntu}_amd64.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

#

ar -x ../libdrm2-amdgpu*%{ubuntu}_amd64.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

###

#

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu/libdrm/lib64

mv ./opt/amdgpu/lib/x86_64-linux-gnu/libdrm.so.2.4.0 ./opt/amdgpu/libdrm/lib64/

mv ./opt/amdgpu/lib/x86_64-linux-gnu/libdrm_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib64/

mv ./opt/amdgpu/lib/x86_64-linux-gnu/libdrm_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib64/

#

ln -s /opt/amdgpu/libdrm/lib64/libdrm.so.2.4.0 ./opt/amdgpu/libdrm/lib64/libdrm.so.2

ln -s /opt/amdgpu/libdrm/lib64/libdrm_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib64/libdrm_amdgpu.so.1

ln -s /opt/amdgpu/libdrm/lib64/libdrm_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib64/libdrm_radeon.so.1

#

ln -s /opt/amdgpu/libdrm/lib64/libdrm.so.2.4.0 ./opt/amdgpu/libdrm/lib64/libdrm.so

ln -s /opt/amdgpu/libdrm/lib64/libdrm_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib64/libdrm_amdgpu.so

ln -s /opt/amdgpu/libdrm/lib64/libdrm_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib64/libdrm_radeon.so

#

mkdir -p "./opt/amdgpu/share/licenses/libdrm-amdgpu-pro"

mv ./usr/share/doc/libdrm2-amdgpu/copyright ./opt/amdgpu/share/licenses/libdrm-amdgpu-pro/libdrm2-amdgpu-copyright

mv ./usr/share/doc/libdrm-amdgpu-amdgpu1/copyright ./opt/amdgpu/share/licenses/libdrm-amdgpu-pro/libdrm-amdgpu-amdgpu1-copyright

mv ./usr/share/doc/libdrm-amdgpu-radeon1/copyright ./opt/amdgpu/share/licenses/libdrm-amdgpu-pro/libdrm-amdgpu-radeon1-copyright

# 

rm -r ./usr/share

#

echo "linking ids"

mkdir -p ./opt/amdgpu/share/libdrm

ln -s /usr/share/libdrm/amdgpu.ids ./opt/amdgpu/share/libdrm/amdgpu.ids


cd %{buildroot}/debs/extract

mv opt %{buildroot}/
mv etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'

%description
AMD proprietary libdrm

%files
"/opt/amdgpu/share/libdrm/amdgpu.ids"
"/opt/amdgpu/share/licenses/libdrm-amdgpu-pro/*-copyright"
"/opt/amdgpu/libdrm/lib64/*.so*"
%exclude "/debs"
%exclude "/opt/amdgpu/lib/x86_64-linux-gnu"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
