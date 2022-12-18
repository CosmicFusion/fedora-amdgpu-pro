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


Name:     amdamf-pro-runtime
Version:  %{repo}
Release:  4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       System runtime for AMD Advanced Media Framework
URL:      http://repo.radeon.com/amdgpu


%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/a/amf-amdgpu-pro/amf-amdgpu-pro_%{amf}-%{minor}~%{ubuntu}_amd64.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/liba/libamdenc-amdgpu-pro/libamdenc-amdgpu-pro_%{enc}-%{minor}~%{ubuntu}_amd64.deb

Provides:      amf-runtime = %{major}-%{release}
Provides:      amf-runtime(x86_64) = %{major}-%{release}
Provides:      amf-amdgpu-pro = %{amf}-%{minor}~%{ubuntu}
Provides:      amf-amdgpu-pro(x86_64) = %{amf}-%{minor}~%{ubuntu}
Provides:      libamfrt64.so.1()(64bit) 
Provides:      libamdenc-amdgpu-pro = %{enc}-%{minor}~%{ubuntu}
Provides:      libamdenc-amdgpu-pro(x86_64) = %{enc}-%{minor}~%{ubuntu}
Provides:      libamdenc64.so.1.0()(64bit)  
Provides:      libamdenc64.so.1.0()(64bit)  

Recommends:	rocm-opencl

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      vulkan-amdgpu-pro  
Requires:      libdrm-pro
Requires:      opencl-filesystem

Recommends:	 rocm-opencl-runtime  

%description
System runtime for AMD Advanced Media Framework

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu-pro/amf/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu-pro/amf/share/licenses/amf-amdgpu-pro
mkdir -p %{buildroot}/opt/amdgpu-pro/amf/share/licenses/libamdenc-amdgpu-pro
#
cp -r files/opt/amdgpu-pro/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu-pro/amf/%{_lib}/
cp -r files/usr/share/doc/amf-amdgpu-pro/copyright %{buildroot}/opt/amdgpu-pro/amf/share/licenses/amf-amdgpu-pro/LICENSE
cp -r files/usr/share/doc/libamdenc-amdgpu-pro/copyright %{buildroot}/opt/amdgpu-pro/amf/share/licenses/libamdenc-amdgpu-pro/LICENSE
#
mkdir -p %{buildroot}/opt/amdgpu-pro/share/licenses
ln -s /opt/amdgpu-pro/amf/share/licenses/amf-amdgpu-pro %{buildroot}/opt/amdgpu-pro/share/licenses/amf-amdgpu-pro
ln -s /opt/amdgpu-pro/amf/share/licenses/libamdenc-amdgpu-pro %{buildroot}/opt/amdgpu-pro/share/licenses/libamdenc-amdgpu-pro
#
echo "adding library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amf-runtime-%{_arch}.conf
echo "/opt/amdgpu-pro/amf/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amf-runtime-%{_arch}.conf

%files
"/etc/ld.so.conf.d/amf-runtime-%{_arch}.conf"
"/opt/amdgpu-pro/amf/lib64/libamf*"
"/opt/amdgpu-pro/amf/lib64/libamdenc*"
"/opt/amdgpu-pro/amf/share/licenses/amf-amdgpu-pro/LICENSE"
"/opt/amdgpu-pro/amf/share/licenses/libamdenc-amdgpu-pro/LICENSE"
"/opt/amdgpu-pro/share/*"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
