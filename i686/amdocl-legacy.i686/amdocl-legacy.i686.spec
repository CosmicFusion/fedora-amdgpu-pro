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

Name:     amdocl-legacy
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD OpenCL ICD Loaders
URL:      http://repo.radeon.com/amdgpu
Provides:      config(opencl-legacy-amdgpu-pro-icd) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      opencl-legacy-amdgpu-pro-icd = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      opencl-legacy-amdgpu-pro-icd(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      opencl-orca-amdgpu-pro-icd  
Provides:      libopencl-amdgpu-pro = %{major}-%{minor}.el%{rhel_minor}
Provides:      ocl-icd-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      ocl-icd-amdgpu-pro(i686) = 0:%{major}-%{minor}.el%{rhel_minor}

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      libdrm-pro  

BuildRequires: wget 
BuildRequires: cpio

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/proprietary/o/opencl-legacy-amdgpu-pro/opencl-legacy-amdgpu-pro-icd_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/proprietary/o/ocl-icd-amdgpu-pro/ocl-icd-libopencl1-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

ar -x ../opencl-legacy-amdgpu-pro-icd_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

rm -r ./usr

ar -x ../ocl-icd-libopencl1-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

rm -r ./usr

###

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu-pro/OpenCL

mv ./opt/amdgpu-pro/lib/i386-linux-gnu ./opt/amdgpu-pro/OpenCL/lib32

rm -r ./opt/amdgpu-pro/lib

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu-pro/OpenCL/lib32/*.so

# 

echo "adding library path"

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdocl-legacy-i686.conf

echo "/opt/amdgpu-pro/OpenCL/lib32" > ./etc/ld.so.conf.d/amdocl-legacy-i686.conf

###

mv ./opt %{buildroot}/
mv ./etc %{buildroot}/

%description
OpenCL (Open Computing Language) is a multivendor open standard for
general-purpose parallel programming of heterogeneous systems that include
CPUs, GPUs and other processors. + The ICD Loader library provided by AMD.

%files
"/etc/OpenCL/vendors/amdocl-orca32.icd"
"/etc/ld.so.conf.d/amdocl-legacy-i686.conf"
"/opt/amdgpu-pro/OpenCL/lib32/libOpenCL.so.1"
"/opt/amdgpu-pro/OpenCL/lib32/libOpenCL.so.1.2"
"/opt/amdgpu-pro/OpenCL/lib32/libamdocl-orca32.so"
%exclude "/debs"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
