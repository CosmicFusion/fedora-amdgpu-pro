%define _build_id_links none

# global info
%global repo 5.5.3
%global major 23.10
%global minor 1620044
# pkg info
%global amf 1.4.30
%global enc 1.0
%global amdvlk 2023.Q3.1
# drm info
%global drm 2.4.114.50503-1620033
%global amdgpu 1.0.0.50503-1636786
# firmware info
%global firmware_rev 6.0.5
%global firmware_maj 50503
%global firmware_min 1620033
%global _firmwarepath	/usr/lib/firmware
# Distro info
%global fedora 38
%global ubuntu 22.04



Name:          amdocl-legacy
Version:  	   %{repo}
Release:       4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       AMD OpenCL ICD Loaders

URL:           http://repo.radeon.com/amdgpu

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opencl-legacy-amdgpu-pro/opencl-legacy-amdgpu-pro-icd_%{major}-%{minor}.%{ubuntu}_i386.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/ocl-icd-amdgpu-pro/ocl-icd-libopencl1-amdgpu-pro_%{major}-%{minor}.%{ubuntu}_i386.deb

Provides:      amdocl-legacy = %{major}-%{release}
Provides:      amdocl-legacy(i686) = %{major}-%{release}
Provides:      config(opencl-legacy-amdgpu-pro-icd) = %{major}-%{minor}.%{ubuntu}
Provides:      libopencl-amdgpu-pro = %{major}-%{minor}.%{ubuntu}
Provides:      ocl-icd-amdgpu-pro = %{major}-%{minor}.%{ubuntu}
Provides:      ocl-icd-amdgpu-pro(i686) = %{major}-%{minor}.%{ubuntu}
Provides:      opencl-legacy-amdgpu-pro-icd = %{major}-%{minor}.%{ubuntu}
Provides:      opencl-legacy-amdgpu-pro-icd(i686) = %{major}-%{minor}.%{ubuntu}
Provides:      opencl-orca-amdgpu-pro-icd  

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig  

Requires:      libdrm-pro(i686)

Recommends: amdgpu-opencl-switcher(x86_64)

%description
OpenCL (Open Computing Language) is a multivendor open standard for
general-purpose parallel programming of heterogeneous systems that include
CPUs, GPUs and other processors. + The ICD Loader library provided by AMD.

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu-pro/opencl/%{_lib}
mkdir -p %{buildroot}/etc/OpenCL/vendors/
#
cp -r files/etc/OpenCL/vendors/* %{buildroot}/etc/OpenCL/vendors/
cp -r files/opt/amdgpu-pro/lib/i386-linux-gnu/* %{buildroot}/opt/amdgpu-pro/opencl/%{_lib}/
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdocl-legacy-%{_arch}.conf
echo "#/opt/amdgpu-pro/opencl/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdocl-legacy-%{_arch}.conf

%files
"/etc/OpenCL/vendors/amdocl-orca32.icd"
"/etc/ld.so.conf.d/amdocl-legacy-%{_arch}.conf"
"/opt/amdgpu-pro/opencl/%{_lib}/libOpenCL*"
"/opt/amdgpu-pro/opencl/%{_lib}/libamdocl-orca*"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
