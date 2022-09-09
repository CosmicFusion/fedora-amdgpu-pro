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
%global drm-common 1.0.0.50203
# Distro info
%global fedora fc36
%global ubuntu 22.04


Name:          amdocl-legacy
Version:  	   %{repo}
Release:       4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       AMD OpenCL ICD Loaders

URL:           http://repo.radeon.com/amdgpu

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opencl-legacy-amdgpu-pro/opencl-legacy-amdgpu-pro-icd_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/ocl-icd-amdgpu-pro/ocl-icd-libopencl1-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_amd64.deb

 

Provides:      amdocl-legacy = %{major}-%{release}
Provides:      amdocl-legacy(x86-64) = %{major}-%{release}
Provides:      config(opencl-legacy-amdgpu-pro-icd) = 0:%{major}-%{minor}~%{ubuntu}
Provides:      libopencl-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      ocl-icd-amdgpu-pro = 0:%{major}-%{minor}~%{ubuntu}
Provides:      ocl-icd-amdgpu-pro(x86-64) = 0:%{major}-%{minor}~%{ubuntu}
Provides:      opencl-legacy-amdgpu-pro-icd = 0:%{major}-%{minor}~%{ubuntu}
Provides:      opencl-legacy-amdgpu-pro-icd(x86-64) = 0:%{major}-%{minor}~%{ubuntu}
Provides:      opencl-orca-amdgpu-pro-icd  

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig  

Requires:      libdrm-pro 

Recommends: amdgpu-opencl-switcher

%description
OpenCL (Open Computing Language) is a multivendor open standard for
general-purpose parallel programming of heterogeneous systems that include
CPUs, GPUs and other processors. + The ICD Loader library provided by AMD.

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz

%install
mkdir -p %{buildroot}/opt/amdgpu-pro/opencl/%{_lib}
mkdir -p %{buildroot}/etc/OpenCL/vendors/
mkdir -p %{buildroot}/opt/amdgpu-pro/opencl/share/licenses/opencl-legacy-amdgpu-pro-icd
mkdir -p %{buildroot}/opt/amdgpu-pro/opencl/share/licenses/ocl-icd-libopencl1-amdgpu-pro
#
install -p -m755 files/etc/OpenCL/vendors/* %{buildroot}/etc/OpenCL/vendors/
install -p -m755 files/opt/amdgpu-pro/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu-pro/opencl/%{_lib}/
install -p -m755 files/usr/share/doc/opencl-legacy-amdgpu-pro-icd/copyright %{buildroot}/opt/amdgpu-pro/opencl/share/licenses/opencl-legacy-amdgpu-pro-icd/LICENSE
install -p -m755 files/usr/share/doc/ocl-icd-libopencl1-amdgpu-pro/copyright %{buildroot}/opt/amdgpu-pro/opencl/share/licenses/ocl-icd-libopencl1-amdgpu-pro/LICENSE
#
mkdir -p %{buildroot}/opt/amdgpu-pro/share/licenses
ln -s /opt/amdgpu-pro/opencl/share/licenses/opencl-legacy-amdgpu-pro-icd %{buildroot}/opt/amdgpu-pro/share/licenses/opencl-legacy-amdgpu-pro-icd
ln -s /opt/amdgpu-pro/opencl/share/licenses/ocl-icd-libopencl1-amdgpu-pro %{buildroot}/opt/amdgpu-pro/share/licenses/ocl-icd-libopencl1-amdgpu-pro
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdocl-legacy-%{_arch}.conf
echo "#/opt/amdgpu-pro/opencl/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdocl-legacy-%{_arch}.conf

%files
"/etc/OpenCL/vendors/amdocl-orca64.icd"
"/etc/ld.so.conf.d/amdocl-legacy-%{_arch}.conf"
"/opt/amdgpu-pro/opencl/%{_lib}/libOpenCL*"
"/opt/amdgpu-pro/opencl/%{_lib}/libamdocl-orca*"
"/opt/amdgpu-pro/opencl/share/licenses/opencl-legacy-amdgpu-pro-icd/LICENSE"
"/opt/amdgpu-pro/opencl/share/licenses/ocl-icd-libopencl1-amdgpu-pro/LICENSE"
"/opt/amdgpu-pro/share/*"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
