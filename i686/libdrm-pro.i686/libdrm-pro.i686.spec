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

Name:     libdrm-pro
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
Summary:       AMD proprietary libdrm
URL:      http://repo.radeon.com/amdgpu

<<<<<<< HEAD
Provides:      libdrm-pro
Provides:      libdrm-pro(i686)
Provides:      libdro.so.2()
Provides:      libdro_amdgpu.so.1()
Provides:      libdro_radeon.so.1()
Provides:      libdro.so.2()(i686)
Provides:      libdro_amdgpu.so.1()(i686)
Provides:      libdro_radeon.so.1()(i686)
Provides:      libdro.so.2()(x86_32)
Provides:      libdro_amdgpu.so.1()(x86_32)
Provides:      libdro_radeon.so.1()(x86_32)
Provides:      libdro.so.2()(32bit)
Provides:      libdro_amdgpu.so.1()(32bit)
Provides:      libdro_radeon.so.1()(32bit)

Requires: 	libdrm-pro(x86_64)
Requires: 	libdrm
=======
%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm-amdgpu-amdgpu1_%{drm}-%{minor}~%{ubuntu}_i386.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm-amdgpu-radeon1_%{drm}-%{minor}~%{ubuntu}_i386.deb
Source2:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm2-amdgpu_%{drm}-%{minor}~%{ubuntu}_i386.deb

Provides:      libdrm-pro
Provides:      libdrm-pro(i686)

Provides:      libdrm.so.2()
Provides:      libdrm_amdgpu.so.1()
Provides:      libdrm_radeon.so.1()
Provides:      libdrm.so.2()(i686)
Provides:      libdrm_amdgpu.so.1()(i686)
Provides:      libdrm_radeon.so.1()(i686)
Provides:      libdrm.so.2()(32bit)
Provides:      libdrm_amdgpu.so.1()(32bit)
Provides:      libdrm_radeon.so.1()(32bit)

Provides:      libdrm-amdgpu = %{drm}-%{minor}~%{ubuntu}
Provides:      libdrm-amdgpu-common = %{amdgpu}-%{minor}~%{ubuntu}

Provides:      libdrm-amdgpu-amdgpu1 = %{drm}-%{minor}~%{ubuntu}
Provides:      libdrm-amdgpu-radeon1 = %{drm}-%{minor}~%{ubuntu}
Provides:      libdrm2-amdgpu = %{drm}-%{minor}~%{ubuntu}


>>>>>>> bfb7e56 (update 64 to latest release)

BuildRequires: wget 
BuildRequires: cpio

<<<<<<< HEAD
%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget -r -nd --no-parent -A 'libdrm-amdgpu-amdgpu1*%{ubuntu}_i386.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

wget -r -nd --no-parent -A 'libdrm-amdgpu-radeon1*%{ubuntu}_i386.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

wget -r -nd --no-parent -A 'libdrm2-amdgpu*%{ubuntu}_i386.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

#

ar -x ../libdrm-amdgpu-amdgpu1*%{ubuntu}_i386.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

#

ar -x ../libdrm-amdgpu-radeon1*%{ubuntu}_i386.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

#

ar -x ../libdrm2-amdgpu*%{ubuntu}_i386.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

###

#

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu/libdrm/lib32

mv ./opt/amdgpu/lib/i386-linux-gnu/libdrm.so.2.4.0 ./opt/amdgpu/libdrm/lib32/libdro.so.2.4.0

mv ./opt/amdgpu/lib/i386-linux-gnu/libdrm_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib32/libdro_amdgpu.so.1.0.0

mv ./opt/amdgpu/lib/i386-linux-gnu/libdrm_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib32/libdro_radeon.so.1.0.1

#

ln -s /opt/amdgpu/libdrm/lib32/libdro.so.2.4.0 ./opt/amdgpu/libdrm/lib32/libdro.so.2

ln -s /opt/amdgpu/libdrm/lib32/libdro_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib32/libdro_amdgpu.so.1

ln -s /opt/amdgpu/libdrm/lib32/libdro_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib32/libdro_radeon.so.1

#

ln -s /opt/amdgpu/libdrm/lib32/libdro.so.2.4.0 ./opt/amdgpu/libdrm/lib32/libdro.so

ln -s /opt/amdgpu/libdrm/lib32/libdro_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib32/libdro_amdgpu.so

ln -s /opt/amdgpu/libdrm/lib32/libdro_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib32/libdro_radeon.so

# 

rm -r ./usr/share

# 

echo "adding needed library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/libdrm-pro-i686.conf

echo "/opt/amdgpu/libdrm/lib32" > ./etc/ld.so.conf.d/libdrm-pro-i686.conf

mkdir -p ./etc/profile.d

touch ./etc/profile.d/libdrm-pro-i686.sh

echo 'export LD_LIBRARY_PATH="/opt/amdgpu/libdrm/lib32:$LD_LIBRARY_PATH"' > ./etc/profile.d/libdrm-pro-i686.sh

cd %{buildroot}/debs/extract

mv opt %{buildroot}/
mv etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'
=======
Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires: 	libdrm-pro(x86_64)

Requires: 	libdrm
>>>>>>> bfb7e56 (update 64 to latest release)

%description
AMD proprietary libdrm

<<<<<<< HEAD
%files
"/opt/amdgpu/libdrm/lib32/*.so*"
"/etc/ld.so.conf.d/libdrm-pro-i686.conf"
"/etc/profile.d/libdrm-pro-i686.sh"
%exclude "/debs"
%exclude "/opt/amdgpu/lib/i386-linux-gnu"
=======
%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE2}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu/libdrm/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-amdgpu1
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-radeon1
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm2-amdgpu
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/libdrm
#
cp -r files/opt/amdgpu/lib/i386-linux-gnu/* %{buildroot}/opt/amdgpu/libdrm/%{_lib}/
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf
echo "#/opt/amdgpu/libdrm/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf

%files
"/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf"
"/opt/amdgpu/libdrm/%{_lib}/*drm*"
>>>>>>> bfb7e56 (update 64 to latest release)

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
