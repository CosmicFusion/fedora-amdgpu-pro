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

Name:     amdamf-pro-runtime
Version:  %{amdpro}
Release:  3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       System runtime for AMD Advanced Media Framework
URL:      http://repo.radeon.com/amdgpu

Provides:      amf-runtime = %{major}-3.%{fedora}
Provides:      amf-runtime(x86-64) = %{major}-3.%{fedora}
Provides:      amf-amdgpu-pro = 0:%{amf}-%{minor}.el%{rhel_minor}
Provides:      amf-amdgpu-pro(x86-64) = 0:%{amf}-%{minor}.el%{rhel_minor}
Provides:      libamfrt64.so.1()(64bit) 
Provides:      libamdenc-amdgpu-pro = 0:%{enc}-%{minor}.el%{rhel_minor}
Provides:      libamdenc-amdgpu-pro(x86-64) = 0:%{enc}-%{minor}.el%{rhel_minor}
Provides:      libamdenc64.so.1.0()(64bit)  
Provides:      libamdenc64.so.1.0()(64bit)  

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      vulkan-amdgpu-pro  
Requires:      libdrm-pro
Requires:      opencl-filesystem


Recommends:	 rocm-opencl-runtime  


%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/rpms

cd %{buildroot}/rpms

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/rhel/"%{rhel_major}"/proprietary/x86_64/amf-amdgpu-pro-"%{amf}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/rhel/"%{rhel_major}"/proprietary/x86_64/libamdenc-amdgpu-pro-"%{enc}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm

###

echo "extracting packages"

mkdir -p %{buildroot}/rpms/extract

cd %{buildroot}/rpms/extract

rpm2cpio ../amf-amdgpu-pro-"%{amf}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

rpm2cpio ../libamdenc-amdgpu-pro-"%{enc}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

###

#

echo "restructuring package directories  "

cd %{buildroot}/rpms/extract

mkdir -p ./opt/amdgpu-pro/amf

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/amf/

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu-pro/amf/lib64/*.so

#

echo "adding library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amf-runtime-x86_64.conf

echo "/opt/amdgpu-pro/amf/lib64" > ./etc/ld.so.conf.d/amf-runtime-x86_64.conf

cd %{buildroot}/rpms/extract

mv ./opt %{buildroot}/
mv ./usr %{buildroot}/
mv ./etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'

%description
Amd encode library

%files
"/etc/ld.so.conf.d/amf-runtime-x86_64.conf"
"/opt/amdgpu-pro/amf/lib64/libamdenc64.so"
"/opt/amdgpu-pro/amf/lib64/libamdenc64.so.1.0"
"/opt/amdgpu-pro/amf/lib64/libamfrt64.so*"
"/opt/amdgpu-pro/share/licenses/amf-amdgpu-pro/AMDGPUPROEULA"
"/opt/amdgpu-pro/share/licenses/libamdenc-amdgpu-pro/AMDGPUPROEULA"
%exclude "/rpms"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
