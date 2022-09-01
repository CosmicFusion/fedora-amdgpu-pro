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
Provides:      amdvlk(x86_64) = %{amdvlk}-3
Provides:      config(amdvlk) = %{amdvlk}-3
Requires:      config(amdvlk) = %{amdvlk}-3
Requires:      vulkan-loader

BuildRequires: wget 
BuildRequires: cpio

Requires:      libdrm-pro  

Recommends:	 openssl-libs  

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget http://repo.radeon.com/amdvlk/apt/debian/pool/main/a/amdvlk/amdvlk_"%{amdvlk}"_amd64.deb

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

ar -x ../amdvlk_"%{amdvlk}"_amd64.deb

tar -xf data.tar.gz

rm -r *.tar*

rm debian-binary

###

#

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu/vulkan

mv ./usr/lib/x86_64-linux-gnu ./opt/amdgpu/vulkan/lib64

rm -r ./usr/share

#

echo "fixing .icds "

sed -i "s#/usr/lib/x86_64-linux-gnu/amdvlk64.so#/opt/amdgpu/vulkan/lib64/amdvlk64.so#" "./etc/vulkan/icd.d/amd_icd64.json"

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu/vulkan/lib64/*.so

# we don't need this one
rm ./etc/vulkan/implicit_layer.d/amd_icd64.json

###

mv ./opt %{buildroot}/
mv ./etc %{buildroot}/opt/amdgpu/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'

%files
"/opt/amdgpu/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu/vulkan/lib64/amdvlk64.so"
%exclude "/debs"

%description
AMD Open Source Driver for Vulkan

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
