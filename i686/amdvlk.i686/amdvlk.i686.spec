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

Name:          amdvlk
Version:       %{amdvlk}
Release:       3
License:       MIT 
Group:         System Environment/Libraries
Summary:       AMD Open Source Driver for Vulkan

URL:           https://github.com/GPUOpen-Drivers/AMDVLK
Vendor:        Advanced Micro Devices (AMD)

Provides:      amdvlk = %{amdvlk}-3
Provides:      amdvlk(i686) = %{amdvlk}-3
Provides:      config(amdvlk) = %{amdvlk}-3
Requires:      config(amdvlk) = %{amdvlk}-3
Requires:      vulkan-loader

Requires:      libdrm-pro  

BuildRequires: wget 
BuildRequires: cpio

Recommends:	 openssl-libs  

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget http://repo.radeon.com/amdvlk/apt/debian/pool/main/a/amdvlk/amdvlk_"%{amdvlk}"_i386.deb

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

ar -x ../amdvlk_"%{amdvlk}"_i386.deb

tar -xf data.tar.gz

rm -r *.tar*

rm debian-binary

###

#

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu/vulkan

mv ./usr/lib/i386-linux-gnu ./opt/amdgpu/vulkan/lib32

rm -r ./usr/share

#

echo "fixing .icds "

sed -i "s#/usr/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu/vulkan/lib32/amdvlk32.so#" "./etc/vulkan/icd.d/amd_icd32.json"

# we don't need this one
rm ./etc/vulkan/implicit_layer.d/amd_icd32.json

###

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu/vulkan/lib32/*.so

#

mv ./opt %{buildroot}/
mv ./etc %{buildroot}/opt/amdgpu/

%files
"/opt/amdgpu/etc/vulkan/icd.d/amd_icd32.json"
"/opt/amdgpu/vulkan/lib32/amdvlk32.so"
%exclude "/debs"

%description
AMD Open Source Driver for Vulkan

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
