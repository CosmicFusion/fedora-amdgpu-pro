%define _build_id_links none

# global info
%global repo 5.7.1
%global major 23.20
%global minor 1664987
# pkg info
%global amf 1.4.31
%global enc 1.0
%global amdvlk 2023.Q3.3
# drm info
%global drm 2.4.115.50701-1664922
%global amdgpu 1.0.0.50701-1664922
# firmware info
%global firmware_rev 6.4.2
%global firmware_maj 50701
%global firmware_min 1664922
%global _firmwarepath	/usr/lib/firmware
# Distro info
%global fedora 39
%global ubuntu 22.04

Name:     libdrm-pro
Version:  %{repo}
Release:  4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       AMD proprietary libdrm
URL:      http://repo.radeon.com/amdgpu

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm-amdgpu-amdgpu1_%{drm}.%{ubuntu}_i386.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm-amdgpu-radeon1_%{drm}.%{ubuntu}_i386.deb
Source2:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm2-amdgpu_%{drm}.%{ubuntu}_i386.deb

Provides:      libdrm-pro
Provides:      libdrm-pro(i686)

Provides:      libdrm.so.2()
Provides:      libdrm_amdgpu.so.1()
Provides:      libdrm_radeon.so.1()
Provides:      libdrm.so.2()(i686)
Provides:      libdrm_amdgpu.so.1()(i686)
Provides:      libdrm_radeon.so.1()(i686)
Provides:      libdrm.so.2()(32bit)
Provides:      libdrm_amdgpu.so.1()(32bit)
Provides:      libdrm_radeon.so.1()(32bit)

Provides:      libdrm-amdgpu = %{drm}.%{ubuntu}
Provides:      libdrm-amdgpu-common = %{amdgpu}.%{ubuntu}

Provides:      libdrm-amdgpu-amdgpu1 = %{drm}.%{ubuntu}
Provides:      libdrm-amdgpu-radeon1 = %{drm}.%{ubuntu}
Provides:      libdrm2-amdgpu = %{drm}.%{ubuntu}



BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires: 	libdrm-pro(x86_64)

Requires: 	libdrm

%description
AMD proprietary libdrm

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE2}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu/libdrm/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-amdgpu1
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-radeon1
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm2-amdgpu
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/libdrm
#
cp -r files/opt/amdgpu/lib/i386-linux-gnu/* %{buildroot}/opt/amdgpu/libdrm/%{_lib}/
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf
echo "#/opt/amdgpu/libdrm/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf

%files
"/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf"
"/opt/amdgpu/libdrm/%{_lib}/*drm*"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
