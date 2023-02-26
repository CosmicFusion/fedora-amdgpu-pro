%define _build_id_links none

# global info
%global repo 5.4.3
%global major 22.40
%global minor 1538781
# pkg info
%global amf 1.4.29
%global enc 1.0
%global amdvlk 2022.Q4.4
# drm info
%global drm 2.4.113.50403-1538762
%global amdgpu 1.0.0.50403-1538762
# Distro info
%global fedora 37
%global ubuntu 22.04


Name:     amdvlk-pro
Version:  %{repo}
Release:  4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/v/vulkan-amdgpu-pro/vulkan-amdgpu-pro_%{major}-%{minor}.%{ubuntu}_amd64.deb

Provides:      config(amdvlk-pro) = %{major}-%{release}
Provides:      amdvlk-pro = %{major}-%{release}
Provides:      amdvlk-pro(x86_64) = %{major}-%{release}
Provides:      config(vulkan-amdgpu-pro) = %{major}-%{minor}.%{ubuntu}
Provides:      vulkan-amdgpu-pro = %{major}-%{minor}.%{ubuntu}
Provides:      vulkan-amdgpu-pro(x86_64) = %{major}-%{minor}.%{ubuntu}


Recommends:	 openssl-libs  

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      vulkan-loader
Requires:      libdrm-pro  

Recommends:	 amdgpu-vulkan-switcher

%description
Amdgpu Pro Vulkan driver

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu-pro/vulkan/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/
mkdir -p %{buildroot}/opt/amdgpu-pro/vulkan/share/licenses/vulkan-amdgpu-pro
mkdir -p %{buildroot}/opt/amdgpu-pro/etc/vulkan/icd.d/
#
cp -r files/opt/amdgpu-pro/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu-pro/vulkan/%{_lib}/
cp -r files/opt/amdgpu-pro/etc/vulkan/icd.d/* %{buildroot}/opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/
cp -r files/usr/share/doc/vulkan-amdgpu-pro/copyright %{buildroot}/opt/amdgpu-pro/vulkan/share/licenses/vulkan-amdgpu-pro/LICENSE
#
mkdir -p %{buildroot}/opt/amdgpu-pro/share/licenses
ln -s /opt/amdgpu-pro/vulkan/share/licenses/vulkan-amdgpu-pro %{buildroot}/opt/amdgpu-pro/share/licenses/vulkan-amdgpu-pro
#
echo "fixing .icds "
sed -i "s#/opt/amdgpu-pro/lib/x86_64-linux-gnu/amdvlk64.so#/opt/amdgpu-pro/vulkan/%{_lib}/amdvlk64.so#" "%{buildroot}/opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/amd_icd64.json"
#
ln -s /opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/amd_icd64.json %{buildroot}/opt/amdgpu-pro/etc/vulkan/icd.d/
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdvlk-pro-%{_arch}.conf
echo "#/opt/amdgpu-pro/vulkan/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdvlk-pro-%{_arch}.conf

%files
"/etc/ld.so.conf.d/amdvlk-pro-%{_arch}.conf"
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu-pro/vulkan/%{_lib}/amdvlk64*"
"/opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu-pro/vulkan/share/licenses/vulkan-amdgpu-pro/LICENSE"
"/opt/amdgpu-pro/share/*"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
