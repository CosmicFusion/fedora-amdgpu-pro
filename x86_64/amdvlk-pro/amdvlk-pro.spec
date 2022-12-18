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
=======
%define _build_id_links none

# global info
%global repo 5.4.1
%global major 22.40
%global minor 1518373
# Distro info
>>>>>>> bfb7e56 (update 64 to latest release)
%global fedora fc36
%global ubuntu 22.04

Name:     amdvlk-pro
<<<<<<< HEAD
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
=======
Version:  %{repo}
Release:  4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
>>>>>>> bfb7e56 (update 64 to latest release)
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu

<<<<<<< HEAD
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
=======
%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/v/vulkan-amdgpu-pro/vulkan-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_amd64.deb

Provides:      config(amdvlk-pro) = %{major}-%{release}
Provides:      amdvlk-pro = %{major}-%{release}
Provides:      amdvlk-pro(x86_64) = %{major}-%{release}
Provides:      config(vulkan-amdgpu-pro) = %{major}-%{minor}~%{ubuntu}
Provides:      vulkan-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      vulkan-amdgpu-pro(x86_64) = %{major}-%{minor}~%{ubuntu}


Recommends:	 openssl-libs  
>>>>>>> bfb7e56 (update 64 to latest release)

BuildRequires: wget 
BuildRequires: cpio

<<<<<<< HEAD
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
=======
Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      vulkan-loader
Requires:      libdrm-pro  

Recommends:	 amdgpu-vulkan-switcher
>>>>>>> bfb7e56 (update 64 to latest release)

%description
Amdgpu Pro Vulkan driver

<<<<<<< HEAD
%files
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu-pro/share/licenses/vulkan-amdgpu-pro/AMDGPUPROEULA"
"/opt/amdgpu-pro/vulkan/lib64/amdvlk64*"
"/etc/ld.so.conf.d/amdvlk-pro-x86_64.conf"
%exclude "/rpms"
=======
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
>>>>>>> bfb7e56 (update 64 to latest release)

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
