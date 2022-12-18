%define _build_id_links none

# global info
%global repo 5.4.1
%global major 22.40
%global minor 1518373
# pkg info
%global amf 1.4.29
%global enc 1.0
%global amdvlk 2022.Q4.4
# drm info
%global drm 2.4.113.50401
%global amdgpu 1.0.0.50401
# Distro info
%global fedora fc36
%global ubuntu 22.04

Name:     amdvlk-pro-legacy
Version:  %{repo}
Release:  4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/v/vulkan-amdgpu-pro/vulkan-amdgpu-pro_%{major}-%{minor}_i386.deb

Provides:      config(amdvlk-pro) = %{major}-%{release}
Provides:      amdvlk-pro = %{major}-%{release}
Provides:      amdvlk-pro(i686) = %{major}-%{release}
Provides:      config(vulkan-amdgpu-pro) = %{major}-%{minor}~%{ubuntu}
Provides:      vulkan-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      vulkan-amdgpu-pro(i686) = %{major}-%{minor}~%{ubuntu}


Recommends:	 openssl-libs  

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      vulkan-loader
Requires:      libdrm-pro(i686) 

Recommends:	 amdgpu-vulkan-switcher(x86_64)

%description
Amdgpu Pro Vulkan driver

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu-pro/vulkan-legacy/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu-pro/vulkan-legacy/etc/vulkan/icd.d/
#
cp -r files/opt/amdgpu-pro/lib/i386-linux-gnu/* %{buildroot}/opt/amdgpu-pro/vulkan-legacy/%{_lib}/
cp -r files/opt/amdgpu-pro/etc/vulkan/icd.d/* %{buildroot}/opt/amdgpu-pro/vulkan-legacy/etc/vulkan/icd.d/
#
echo "fixing .icds "
sed -i "s#/opt/amdgpu-pro/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu-pro/vulkan-legacy/%{_lib}/amdvlk32.so#" "%{buildroot}/opt/amdgpu-pro/vulkan-legacy/etc/vulkan/icd.d/amd_icd32.json"
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdvlk-pro-legacy-%{_arch}.conf
echo "#/opt/amdgpu-pro/vulkan-legacy/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdvlk-pro-legacy-%{_arch}.conf

%files
"/etc/ld.so.conf.d/amdvlk-pro-legacy-%{_arch}.conf"
"/opt/amdgpu-pro/vulkan-legacy/%{_lib}/amdvlk32*"
"/opt/amdgpu-pro/vulkan-legacy/etc/vulkan/icd.d/amd_icd32.json"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
