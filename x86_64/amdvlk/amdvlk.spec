# global info
%global repo 22.20.3
%global major 22.20
%global minor 1462318
# pkg info
%global amf 1.4.26
%global enc 1.0
#
%global amdvlk 2022.Q3.3
#
%global drm 2.4.110.50203
%global drm-common 2.4.110.50203
# Distro info
%global fedora fc36
%global ubuntu 22.04

Name:          amdvlk
Version:       %{amdvlk}
Release:       4
License:       MIT 
Group:         System Environment/Libraries
Summary:       AMD Open Source Driver for Vulkan

URL:           https://github.com/GPUOpen-Drivers/AMDVLK
Vendor:        Advanced Micro Devices (AMD)

%undefine _disable_source_fetch
Source0 :  http://repo.radeon.com/amdvlk/apt/debian/pool/main/a/amdvlk/amdvlk_%{amdvlk}_amd64.deb

Provides:      amdvlk = %{amdvlk}-%{release}
Provides:      amdvlk(x86_64) = %{amdvlk}-%{release}
Provides:      config(amdvlk) = %{amdvlk}-%{release}

Recommends:	 openssl-libs  

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      config(amdvlk) = %{amdvlk}-%{release}
Requires:      vulkan-loader
Requires:      libdrm-pro  


%description
AMD Open Source Driver for Vulkan

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install

#
echo "fixing .icds "
sed -i "s#/usr/lib/x86_64-linux-gnu/amdvlk64.so#/opt/amdgpu/vulkan/lib64/amdvlk64.so#" "./etc/vulkan/icd.d/amd_icd64.json"


%files
"/opt/amdgpu/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu/vulkan/lib64/amdvlk64.so"
%exclude "/debs"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig
