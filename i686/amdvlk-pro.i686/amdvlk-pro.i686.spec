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
%global amdgpu 1.0.0.50203
# Distro info
>>>>>>> bfb7e56 (update 64 to latest release)
%global fedora fc36
%global ubuntu 22.04

Name:     amdvlk-pro
<<<<<<< HEAD
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu
Provides:      config(amdvlk-pro) = %{major}-3.%{fedora}
Provides:      amdvlk-pro = %{major}-3.%{fedora}
Provides:      amdvlk-pro(i686) = %{major}-3.%{fedora}
Provides:      config(vulkan-amdgpu-pro) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      vulkan-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      vulkan-amdgpu-pro(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Requires:      vulkan-loader
=======
Version:  %{repo}
Release:  4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/v/vulkan-amdgpu-pro/vulkan-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_i386.deb

Provides:      config(amdvlk-pro) = %{major}-%{release}
Provides:      amdvlk-pro = %{major}-%{release}
Provides:      amdvlk-pro(i686) = %{major}-%{release}
Provides:      config(vulkan-amdgpu-pro) = %{major}-%{minor}~%{ubuntu}
Provides:      vulkan-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      vulkan-amdgpu-pro(i686) = %{major}-%{minor}~%{ubuntu}


Recommends:	 openssl-libs  
>>>>>>> bfb7e56 (update 64 to latest release)

BuildRequires: wget 
BuildRequires: cpio

<<<<<<< HEAD
Requires:      libdrm-pro  

Recommends:	 openssl-libs  


%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget http://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/proprietary/v/vulkan-amdgpu-pro/vulkan-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

ar -x ../vulkan-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

rm -r ./usr

###

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu-pro/vulkan

mv ./opt/amdgpu-pro/lib/i386-linux-gnu ./opt/amdgpu-pro/vulkan/lib32

rm -r ./opt/amdgpu-pro/lib

#

echo "fixing .icds "

sed -i "s#/opt/amdgpu-pro/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu-pro/vulkan/lib32/amdvlk32.so#" "./opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu-pro/vulkan/lib32/*.so


# 

echo "adding *Disabled* library path"

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdvlk-pro-i686.conf

echo "# /opt/amdgpu-pro/vulkan/lib32" > ./etc/ld.so.conf.d/amdvlk-pro-i686.conf


###

mv ./opt %{buildroot}/
mv ./etc %{buildroot}/
=======
Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      vulkan-loader
Requires:      libdrm-pro(i686) 

Recommends:	 amdgpu-vulkan-switcher(x86_64)
>>>>>>> bfb7e56 (update 64 to latest release)

%description
Amdgpu Pro Vulkan driver

<<<<<<< HEAD
%files
"/etc/ld.so.conf.d/amdvlk-pro-i686.conf"
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"
"/opt/amdgpu-pro/vulkan/lib32/amdvlk32.so"
%exclude "/debs"
=======
%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu-pro/vulkan/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/
mkdir -p %{buildroot}/opt/amdgpu-pro/etc/vulkan/icd.d/
#
cp -r files/opt/amdgpu-pro/lib/i386-linux-gnu/* %{buildroot}/opt/amdgpu-pro/vulkan/%{_lib}/
cp -r files/opt/amdgpu-pro/etc/vulkan/icd.d/* %{buildroot}/opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/
#
echo "fixing .icds "
sed -i "s#/opt/amdgpu-pro/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu-pro/vulkan/%{_lib}/amdvlk32.so#" "%{buildroot}/opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/amd_icd32.json"
#
ln -s /opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/amd_icd32.json %{buildroot}/opt/amdgpu-pro/etc/vulkan/icd.d/
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdvlk-pro-%{_arch}.conf
echo "#/opt/amdgpu-pro/vulkan/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdvlk-pro-%{_arch}.conf

%files
"/etc/ld.so.conf.d/amdvlk-pro-%{_arch}.conf"
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"
"/opt/amdgpu-pro/vulkan/%{_lib}/amdvlk32*"
"/opt/amdgpu-pro/vulkan/etc/vulkan/icd.d/amd_icd32.json"
>>>>>>> bfb7e56 (update 64 to latest release)

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
