%undefine _auto_set_build_flags
%global major 21.40.2
%global minor 1350682
%global amf 1.4.24
%global enc 1.0
%global rhel_major 8.5
%global rhel_minor 8
%global amdvlk 2022.Q2.3
%global fedora fc36

Name:     amdvlk-pro-rdna2
Version:       %{major}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD Vulkan for rdna2
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

BuildRequires: wget 
BuildRequires: cpio

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/rpms

cd %{buildroot}/rpms

wget http://repo.radeon.com/amdgpu/"%{major}"/rhel/"%{rhel_major}"/proprietary/x86_64/vulkan-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm

###

echo "extracting packages"

mkdir -p %{buildroot}/rpms/extract

cd %{buildroot}/rpms/extract

rpm2cpio ../vulkan-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

###

#

echo "restructuring package directories  "

cd  %{buildroot}/rpms/extract

mkdir -p ./opt/amdgpu-pro/vulkan-rdna2

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/vulkan-rdna2/
#

echo "fixing .icds "

sed -i "s#/opt/amdgpu-pro/lib64/amdvlk64.so#/opt/amdgpu-pro/vulkan-rdna2/lib64/amdvlk64.so#" "./opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json"

# 

echo "adding *Disabled* library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdvlk-pro-rdna2-x86_64.conf

echo "# /opt/amdgpu-pro/vulkan-rdna2/lib64" > ./etc/ld.so.conf.d/amdvlk-pro-rdna2-x86_64.conf




cd %{buildroot}/rpms/extract

mv ./opt %{buildroot}/
mv ./etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'

%description
Amdgpu Pro Vulkan driver for RDNA2

%files
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu-pro/share/licenses/vulkan-amdgpu-pro/AMDGPUPROEULA"
"/opt/amdgpu-pro/vulkan-rdna2/lib64/amdvlk64.so"
"/opt/amdgpu-pro/vulkan-rdna2/lib64/amdvlk64.so.1.0"
"/etc/ld.so.conf.d/amdvlk-pro-rdna2-x86_64.conf"
%exclude "/rpms"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
