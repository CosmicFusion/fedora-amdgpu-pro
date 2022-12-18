<<<<<<< HEAD
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

Name:          amdocl-legacy
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD OpenCL ICD Loaders


URL:           http://repo.radeon.com/amdgpu

BuildRequires: wget 
BuildRequires: cpio

Requires:      libdrm-pro  

Provides:      amdocl-legacy = %{major}-3.%{fedora}
Provides:      amdocl-legacy(x86-64) = %{major}-3.%{fedora}
Provides:      config(opencl-legacy-amdgpu-pro-icd) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libOpenCL.so.1()(64bit)  
Provides:      libOpenCL.so.1()(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.0)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.0)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.1)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.1)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.2)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.2)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.0)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.0)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.1)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.1)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.2)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.2)(64bit)  
Provides:      libamdocl-orca64.so()(64bit)  
Provides:      libamdocl-orca64.so()(64bit)  
Provides:      libamdocl-orca64.so(ACL_0.8)(64bit)  
Provides:      libamdocl-orca64.so(ACL_0.8)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.0)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.0)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.1)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.1)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.2)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.2)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_2.0)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_2.0)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_2.1)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_2.1)(64bit)  
Provides:      libopencl-amdgpu-pro = %{major}-%{minor}.el%{rhel_minor}
Provides:      ocl-icd-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      ocl-icd-amdgpu-pro(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      opencl-legacy-amdgpu-pro-icd = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      opencl-legacy-amdgpu-pro-icd(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      opencl-orca-amdgpu-pro-icd  
Requires(post): /sbin/ldconfig  
Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig  


%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/rpms

cd %{buildroot}/rpms

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/rhel/"%{rhel_major}"/proprietary/x86_64/opencl-legacy-amdgpu-pro-icd-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/rhel/"%{rhel_major}"/proprietary/x86_64/ocl-icd-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm

###

echo "extracting packages"

mkdir -p %{buildroot}/rpms/extract

cd %{buildroot}/rpms/extract

rpm2cpio ../opencl-legacy-amdgpu-pro-icd-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

rpm2cpio ../ocl-icd-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

###

#

echo "restructuring package directories  "

cd  %{buildroot}/rpms/extract

mkdir -p ./opt/amdgpu-pro/OpenCL

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/OpenCL/

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu-pro/OpenCL/lib64/*.so

# 

echo "adding library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdocl-legacy-x86_64.conf

echo "/opt/amdgpu-pro/OpenCL/lib64" > ./etc/ld.so.conf.d/amdocl-legacy-x86_64.conf


cd %{buildroot}/rpms/extract

mv ./opt %{buildroot}/
mv ./usr %{buildroot}/
mv ./etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'
=======
%define _build_id_links none

# global info
%global repo 5.4.1
%global major 22.40
%global minor 1518373
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
Provides:      amdocl-legacy(x86_64) = %{major}-%{release}
Provides:      config(opencl-legacy-amdgpu-pro-icd) = %{major}-%{minor}~%{ubuntu}
Provides:      libopencl-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      ocl-icd-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      ocl-icd-amdgpu-pro(x86_64) = %{major}-%{minor}~%{ubuntu}
Provides:      opencl-legacy-amdgpu-pro-icd = %{major}-%{minor}~%{ubuntu}
Provides:      opencl-legacy-amdgpu-pro-icd(x86_64) = %{major}-%{minor}~%{ubuntu}
Provides:      opencl-orca-amdgpu-pro-icd  

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig  

Requires:      libdrm-pro 

Recommends: amdgpu-opencl-switcher
>>>>>>> bfb7e56 (update 64 to latest release)

%description
OpenCL (Open Computing Language) is a multivendor open standard for
general-purpose parallel programming of heterogeneous systems that include
CPUs, GPUs and other processors. + The ICD Loader library provided by AMD.

<<<<<<< HEAD
%files
"/etc/OpenCL/vendors/amdocl-orca64.icd"
"/etc/ld.so.conf.d/amdocl-legacy-x86_64.conf"
"/opt/amdgpu-pro/OpenCL/lib64/libOpenCL.so.1"
"/opt/amdgpu-pro/OpenCL/lib64/libOpenCL.so.1.2"
"/opt/amdgpu-pro/OpenCL/lib64/libamdocl-orca64.so"
"/opt/amdgpu-pro/share/licenses/ocl-icd-amdgpu-pro/AMDGPUPROEULA"
"/opt/amdgpu-pro/share/licenses/opencl-legacy-amdgpu-pro-icd/AMDGPUPROEULA"
%exclude "/rpms"


=======
%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu-pro/opencl/%{_lib}
mkdir -p %{buildroot}/etc/OpenCL/vendors/
mkdir -p %{buildroot}/opt/amdgpu-pro/opencl/share/licenses/opencl-legacy-amdgpu-pro-icd
mkdir -p %{buildroot}/opt/amdgpu-pro/opencl/share/licenses/ocl-icd-libopencl1-amdgpu-pro
#
cp -r files/etc/OpenCL/vendors/* %{buildroot}/etc/OpenCL/vendors/
cp -r files/opt/amdgpu-pro/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu-pro/opencl/%{_lib}/
cp -r files/usr/share/doc/opencl-legacy-amdgpu-pro-icd/copyright %{buildroot}/opt/amdgpu-pro/opencl/share/licenses/opencl-legacy-amdgpu-pro-icd/LICENSE
cp -r files/usr/share/doc/ocl-icd-libopencl1-amdgpu-pro/copyright %{buildroot}/opt/amdgpu-pro/opencl/share/licenses/ocl-icd-libopencl1-amdgpu-pro/LICENSE
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
>>>>>>> bfb7e56 (update 64 to latest release)

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
