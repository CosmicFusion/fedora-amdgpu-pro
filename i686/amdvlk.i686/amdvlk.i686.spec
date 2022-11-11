%define _build_id_links none

# global info
%global repo 22.20.3
%global major 22.20
%global minor 1462318
# pkg info
%global amf 1.4.26
%global enc 1.0
#
%global amdvlk 2022.Q4.2
#
%global drm 2.4.110.50203
%global amdgpu 1.0.0.50203
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
Source0 :  https://github.com/GPUOpen-Drivers/AMDVLK/releases/download/v-%{amdvlk}/amdvlk_%{amdvlk}_i386.deb

Provides:      amdvlk = %{amdvlk}-%{release}
Provides:      amdvlk(x86_64) = %{amdvlk}-%{release}
Provides:      config(amdvlk) = %{amdvlk}-%{release}
Provides:      vulkan-amdgpu = %{major}-%{minor}~%{ubuntu}
Provides:      vulkan-amdgpu(i386) = %{major}-%{minor}~%{ubuntu}

Recommends:	 openssl-libs  

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      config(amdvlk) = %{amdvlk}-%{release}
Requires:      vulkan-loader
Requires:      libdrm-pro(i686) 

Recommends:	 amdgpu-vulkan-switcher(x86_64)

%description
AMD Open Source Driver for Vulkan

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu/vulkan/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/
mkdir -p %{buildroot}/opt/amdgpu/vulkan/etc/vulkan/icd.d/
mkdir -p %{buildroot}/opt/amdgpu/etc/vulkan/implicit_layer.d/
mkdir -p %{buildroot}/opt/amdgpu/etc/vulkan/icd.d
#
cp -r files/usr/lib/i386-linux-gnu/* %{buildroot}/opt/amdgpu/vulkan/%{_lib}/
cp -r files/etc/vulkan/implicit_layer.d/* %{buildroot}/opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/
cp -r files/etc/vulkan/icd.d/* %{buildroot}/opt/amdgpu/vulkan/etc/vulkan/icd.d/
#
echo "fixing .icds "
sed -i "s#/usr/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu/vulkan/%{_lib}/amdvlk32.so#" "%{buildroot}/opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/amd_icd32.json"
sed -i "s#/usr/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu/vulkan/%{_lib}/amdvlk32.so#" "%{buildroot}/opt/amdgpu/vulkan/etc/vulkan/icd.d/amd_icd32.json"
#
ln -s /opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/amd_icd32.json %{buildroot}/opt/amdgpu/etc/vulkan/implicit_layer.d/
ln -s /opt/amdgpu/vulkan/etc/vulkan/icd.d/amd_icd32.json %{buildroot}/opt/amdgpu/etc/vulkan/icd.d/
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdvlk-%{_arch}.conf
echo "#/opt/amdgpu/vulkan/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdvlk-%{_arch}.conf

%files
"/etc/ld.so.conf.d/amdvlk-%{_arch}.conf"
"/opt/amdgpu/etc/vulkan/icd.d/amd_icd32.json"
"/opt/amdgpu/etc/vulkan/implicit_layer.d/amd_icd32.json"
"/opt/amdgpu/vulkan/%{_lib}/amdvlk32.so"
"/opt/amdgpu/vulkan/etc/vulkan/icd.d/amd_icd32.json"
"/opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/amd_icd32.json"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
