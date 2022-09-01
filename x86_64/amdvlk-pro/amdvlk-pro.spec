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

Name:     amdvlk-pro
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu

Provides:      config(amdvlk-pro) = %{major}-3.%{fedora}
Provides:      amdvlk-pro = %{major}-3.%{fedora}
Provides:      amdvlk-pro(x86-64) = %{major}-3.%{fedora}
Provides:      config(vulkan-amdgpu-pro) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      vulkan-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      vulkan-amdgpu-pro(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Requires:      vulkan-loader

Recommends:	 openssl-libs  
Recommends:	 amdgpu-vulkan-switcher

Requires:      libdrm-pro  

BuildRequires: wget 
BuildRequires: cpio

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/rpms

cd %{buildroot}/rpms

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/rhel/"%{rhel_major}"/proprietary/x86_64/vulkan-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm

###

echo "extracting packages"

mkdir -p %{buildroot}/rpms/extract

cd %{buildroot}/rpms/extract

rpm2cpio ../vulkan-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

###

#

echo "restructuring package directories  "

cd  %{buildroot}/rpms/extract

mkdir -p ./opt/amdgpu-pro/vulkan

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/vulkan/
#

echo "fixing .icds "

sed -i "s#/opt/amdgpu-pro/lib64/amdvlk64.so#/opt/amdgpu-pro/vulkan/lib64/amdvlk64.so#" "./opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json"

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu-pro/vulkan/lib64/*.so


# 



echo "adding *Disabled* library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdvlk-pro-x86_64.conf

echo "# /opt/amdgpu-pro/vulkan/lib64" > ./etc/ld.so.conf.d/amdvlk-pro-x86_64.conf




cd %{buildroot}/rpms/extract

mv opt %{buildroot}/
mv usr %{buildroot}/
mv etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'

%description
Amdgpu Pro Vulkan driver

%files
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu-pro/share/licenses/vulkan-amdgpu-pro/AMDGPUPROEULA"
"/opt/amdgpu-pro/vulkan/lib64/amdvlk64.so"
"/etc/ld.so.conf.d/amdvlk-pro-x86_64.conf"
%exclude "/rpms"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
