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

Name:          amdvlk
Version:       %{amdvlk}
Release:       3
=======
%define _build_id_links none

# pkg info
%global amdvlk 2022.Q4.4
# Distro info
%global fedora fc36
%global ubuntu 22.04


Name:          amdvlk
Version:       %{amdvlk}
Release:       4
>>>>>>> bfb7e56 (update 64 to latest release)
License:       MIT 
Group:         System Environment/Libraries
Summary:       AMD Open Source Driver for Vulkan

URL:           https://github.com/GPUOpen-Drivers/AMDVLK
Vendor:        Advanced Micro Devices (AMD)

<<<<<<< HEAD
Provides:      amdvlk = %{amdvlk}-3
Provides:      amdvlk(x86_64) = %{amdvlk}-3
Provides:      config(amdvlk) = %{amdvlk}-3
Requires:      config(amdvlk) = %{amdvlk}-3
Requires:      vulkan-loader
=======
%undefine _disable_source_fetch
Source0 :  https://github.com/GPUOpen-Drivers/AMDVLK/releases/download/v-%{amdvlk}/amdvlk_%{amdvlk}_amd64.deb

Provides:      amdvlk = %{amdvlk}-%{release}
Provides:      amdvlk(x86_64) = %{amdvlk}-%{release}
Provides:      config(amdvlk) = %{amdvlk}-%{release}
Provides:      vulkan-amdgpu = %{major}-%{minor}~%{ubuntu}
Provides:      vulkan-amdgpu(x86_64) = %{major}-%{minor}~%{ubuntu}

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

wget http://repo.radeon.com/amdvlk/apt/debian/pool/main/a/amdvlk/amdvlk_"%{amdvlk}"_amd64.deb

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

ar -x ../amdvlk_"%{amdvlk}"_amd64.deb

tar -xf data.tar.gz

rm -r *.tar*

rm debian-binary

###

#

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu/vulkan

mv ./usr/lib/x86_64-linux-gnu ./opt/amdgpu/vulkan/lib64

rm -r ./usr/share

#

echo "fixing .icds "

sed -i "s#/usr/lib/x86_64-linux-gnu/amdvlk64.so#/opt/amdgpu/vulkan/lib64/amdvlk64.so#" "./etc/vulkan/icd.d/amd_icd64.json"

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu/vulkan/lib64/*.so

# we don't need this one
rm ./etc/vulkan/implicit_layer.d/amd_icd64.json

###

mv ./opt %{buildroot}/
mv ./etc %{buildroot}/opt/amdgpu/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'

%files
"/opt/amdgpu/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu/vulkan/lib64/amdvlk64.so"
%exclude "/debs"
=======
Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      config(amdvlk) = %{amdvlk}-%{release}
Requires:      vulkan-loader
Requires:      libdrm-pro  

Recommends:	 amdgpu-vulkan-switcher 
>>>>>>> bfb7e56 (update 64 to latest release)

%description
AMD Open Source Driver for Vulkan

<<<<<<< HEAD
=======
%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu/vulkan/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/
mkdir -p %{buildroot}/opt/amdgpu/vulkan/etc/vulkan/icd.d/
mkdir -p %{buildroot}/opt/amdgpu/vulkan/share/licenses/amdvlk
mkdir -p %{buildroot}/opt/amdgpu/etc/vulkan/implicit_layer.d/
mkdir -p %{buildroot}/opt/amdgpu/etc/vulkan/icd.d
#
cp -r files/usr/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu/vulkan/%{_lib}/
cp -r files/etc/vulkan/implicit_layer.d/* %{buildroot}/opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/
cp -r files/etc/vulkan/icd.d/* %{buildroot}/opt/amdgpu/vulkan/etc/vulkan/icd.d/
cp -r files/usr/share/doc/amdvlk/LICENSE* %{buildroot}/opt/amdgpu/vulkan/share/licenses/amdvlk/LICENSE
#
mkdir -p %{buildroot}/opt/amdgpu/share/licenses
ln -s /opt/amdgpu/vulkan/share/licenses/amdvlk %{buildroot}/opt/amdgpu/share/licenses/amdvlk
#
echo "fixing .icds "
sed -i "s#/usr/lib/x86_64-linux-gnu/amdvlk64.so#/opt/amdgpu/vulkan/%{_lib}/amdvlk64.so#" "%{buildroot}/opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/amd_icd64.json"
sed -i "s#/usr/lib/x86_64-linux-gnu/amdvlk64.so#/opt/amdgpu/vulkan/%{_lib}/amdvlk64.so#" "%{buildroot}/opt/amdgpu/vulkan/etc/vulkan/icd.d/amd_icd64.json"
#
ln -s /opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/amd_icd64.json %{buildroot}/opt/amdgpu/etc/vulkan/implicit_layer.d/
ln -s /opt/amdgpu/vulkan/etc/vulkan/icd.d/amd_icd64.json %{buildroot}/opt/amdgpu/etc/vulkan/icd.d/
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdvlk-%{_arch}.conf
echo "#/opt/amdgpu/vulkan/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdvlk-%{_arch}.conf

%files
"/etc/ld.so.conf.d/amdvlk-%{_arch}.conf"
"/opt/amdgpu/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu/etc/vulkan/implicit_layer.d/amd_icd64.json"
"/opt/amdgpu/vulkan/%{_lib}/amdvlk64.so"
"/opt/amdgpu/vulkan/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu/vulkan/etc/vulkan/implicit_layer.d/amd_icd64.json"
"/opt/amdgpu/vulkan/share/licenses/amdvlk/LICENSE"
"/opt/amdgpu/share/*"

>>>>>>> bfb7e56 (update 64 to latest release)
%post
/sbin/ldconfig

%postun
/sbin/ldconfig
