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

Name:     amdvlk-pro
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu
Provides:      config(amdvlk-pro) = %{major}-3.%{fedora}
Provides:      amdvlk-pro = %{major}-3.%{fedora}
Provides:      amdvlk-pro(i686) = %{major}-3.%{fedora}
Provides:      config(vulkan-amdgpu-pro) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      vulkan-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      vulkan-amdgpu-pro(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Requires:      vulkan-loader

BuildRequires: wget 
BuildRequires: cpio

Requires:      libdrm-pro  

Recommends:	 openssl-libs  


%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/proprietary/v/vulkan-amdgpu-pro/vulkan-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

ar -x ../vulkan-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

rm -r ./usr

###

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu-pro/vulkan

mv ./opt/amdgpu-pro/lib/i386-linux-gnu ./opt/amdgpu-pro/vulkan/lib32

rm -r ./opt/amdgpu-pro/lib

#

echo "fixing .icds "

sed -i "s#/opt/amdgpu-pro/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu-pro/vulkan/lib32/amdvlk32.so#" "./opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu-pro/vulkan/lib32/*.so


# 

echo "adding *Disabled* library path"

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdvlk-pro-i686.conf

echo "# /opt/amdgpu-pro/vulkan/lib32" > ./etc/ld.so.conf.d/amdvlk-pro-i686.conf


###

mv ./opt %{buildroot}/
mv ./etc %{buildroot}/

%description
Amdgpu Pro Vulkan driver

%files
"/etc/ld.so.conf.d/amdvlk-pro-i686.conf"
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"
"/opt/amdgpu-pro/vulkan/lib32/amdvlk32.so"
%exclude "/debs"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
