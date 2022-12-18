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
#
%global drm 2.4.113.50401
%global amdgpu 1.0.0.50401
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
Provides:      libdrm-pro(x86_64)

Provides:      libdro.so.2()
Provides:      libdro_amdgpu.so.1()
Provides:      libdro_radeon.so.1()
Provides:      libdro.so.2()(x86_64)
Provides:      libdro_amdgpu.so.1()(x86_64)
Provides:      libdro_radeon.so.1()(x86_64)
Provides:      libdro.so.2()(64bit)
Provides:      libdro_amdgpu.so.1()(64bit)
Provides:      libdro_radeon.so.1()(64bit)

Requires: 	libdrm
=======
%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm-amdgpu-amdgpu1_%{drm}-%{minor}~%{ubuntu}_amd64.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm-amdgpu-radeon1_%{drm}-%{minor}~%{ubuntu}_amd64.deb
Source2:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu/libdrm2-amdgpu_%{drm}-%{minor}~%{ubuntu}_amd64.deb
Source3:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/libd/libdrm-amdgpu-common/libdrm-amdgpu-common_%{amdgpu}-%{minor}~%{ubuntu}_all.deb

Provides:      libdrm-pro
Provides:      libdrm-pro(x86_64)

Provides:      libdrm.so.2()
Provides:      libdrm_amdgpu.so.1()
Provides:      libdrm_radeon.so.1()
Provides:      libdrm.so.2()(x86_64)
Provides:      libdrm_amdgpu.so.1()(x86_64)
Provides:      libdrm_radeon.so.1()(x86_64)
Provides:      libdrm.so.2()(64bit)
Provides:      libdrm_amdgpu.so.1()(64bit)
Provides:      libdrm_radeon.so.1()(64bit)

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

wget -r -nd --no-parent -A 'libdrm-amdgpu-amdgpu1*%{ubuntu}_amd64.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

wget -r -nd --no-parent -A 'libdrm-amdgpu-radeon1*%{ubuntu}_amd64.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

wget -r -nd --no-parent -A 'libdrm2-amdgpu*%{ubuntu}_amd64.deb' https://repo.radeon.com/amdgpu/"%{amdpro}"/ubuntu/pool/main/libd/libdrm-amdgpu/

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

#

ar -x ../libdrm-amdgpu-amdgpu1*%{ubuntu}_amd64.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

#

ar -x ../libdrm-amdgpu-radeon1*%{ubuntu}_amd64.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

#

ar -x ../libdrm2-amdgpu*%{ubuntu}_amd64.deb

tar -xf data.tar.*

rm -r *.tar*

rm debian-binary

###

#

echo "restructuring package directories  "

cd %{buildroot}/debs/extract

mkdir -p ./opt/amdgpu/libdrm/lib64

mv ./opt/amdgpu/lib/x86_64-linux-gnu/libdrm.so.2.4.0 ./opt/amdgpu/libdrm/lib64/libdro.so.2.4.0

mv ./opt/amdgpu/lib/x86_64-linux-gnu/libdrm_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib64/libdro_amdgpu.so.1.0.0

mv ./opt/amdgpu/lib/x86_64-linux-gnu/libdrm_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib64/libdro_radeon.so.1.0.1

#

ln -s /opt/amdgpu/libdrm/lib64/libdro.so.2.4.0 ./opt/amdgpu/libdrm/lib64/libdro.so.2

ln -s /opt/amdgpu/libdrm/lib64/libdro_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib64/libdro_amdgpu.so.1

ln -s /opt/amdgpu/libdrm/lib64/libdro_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib64/libdro_radeon.so.1

#

ln -s /opt/amdgpu/libdrm/lib64/libdro.so.2.4.0 ./opt/amdgpu/libdrm/lib64/libdro.so

ln -s /opt/amdgpu/libdrm/lib64/libdro_amdgpu.so.1.0.0 ./opt/amdgpu/libdrm/lib64/libdro_amdgpu.so

ln -s /opt/amdgpu/libdrm/lib64/libdro_radeon.so.1.0.1 ./opt/amdgpu/libdrm/lib64/libdro_radeon.so

#

mkdir -p "./opt/amdgpu/share/licenses/libdrm-amdgpu-pro"

mv ./usr/share/doc/libdrm2-amdgpu/copyright ./opt/amdgpu/share/licenses/libdrm-amdgpu-pro/libdrm2-amdgpu-copyright

mv ./usr/share/doc/libdrm-amdgpu-amdgpu1/copyright ./opt/amdgpu/share/licenses/libdrm-amdgpu-pro/libdrm-amdgpu-amdgpu1-copyright

mv ./usr/share/doc/libdrm-amdgpu-radeon1/copyright ./opt/amdgpu/share/licenses/libdrm-amdgpu-pro/libdrm-amdgpu-radeon1-copyright

# 

rm -r ./usr/share

#

echo "linking ids"

mkdir -p ./opt/amdgpu/share/libdrm

ln -s /usr/share/libdrm/amdgpu.ids ./opt/amdgpu/share/libdrm/amdgpu.ids

# 

echo "adding needed library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/libdrm-pro-x86_64.conf

echo "/opt/amdgpu/libdrm/lib64" > ./etc/ld.so.conf.d/libdrm-pro-x86_64.conf

mkdir -p ./etc/profile.d

touch ./etc/profile.d/libdrm-pro-x86_64.sh

echo 'export LD_LIBRARY_PATH="/opt/amdgpu/libdrm/lib64:$LD_LIBRARY_PATH"' > ./etc/profile.d/libdrm-pro-x86_64.sh

cd %{buildroot}/debs/extract

mv opt %{buildroot}/
mv etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'
=======
Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires: 	libdrm
>>>>>>> bfb7e56 (update 64 to latest release)

%description
AMD proprietary libdrm

<<<<<<< HEAD
%files
"/opt/amdgpu/share/libdrm/amdgpu.ids"
"/opt/amdgpu/share/licenses/libdrm-amdgpu-pro/*-copyright"
"/opt/amdgpu/libdrm/lib64/*.so*"
"/etc/ld.so.conf.d/libdrm-pro-x86_64.conf"
"/etc/profile.d/libdrm-pro-x86_64.sh"
%exclude "/debs"
%exclude "/opt/amdgpu/lib/x86_64-linux-gnu"
=======
%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE2}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE3}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu/libdrm/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-amdgpu1
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-radeon1
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm2-amdgpu
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-common
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/libdrm
#
cp -r files/opt/amdgpu/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu/libdrm/%{_lib}/
cp -r files/usr/share/doc/libdrm-amdgpu-amdgpu1/copyright %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-amdgpu1/LICENSE
cp -r files/usr/share/doc/libdrm-amdgpu-radeon1/copyright %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-radeon1/LICENSE
cp -r files/usr/share/doc/libdrm2-amdgpu/copyright %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm2-amdgpu/LICENSE
cp -r files/usr/share/doc/libdrm-amdgpu-common/copyright %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-common/LICENSE
cp -r files/opt/amdgpu/share/libdrm/amdgpu.ids %{buildroot}/opt/amdgpu/libdrm/share/libdrm/amdgpu.ids 
#
mkdir -p %{buildroot}/opt/amdgpu/share/licenses
ln -s /opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-amdgpu1 %{buildroot}/opt/amdgpu/share/licenses/libdrm-amdgpu-amdgpu1
ln -s /opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-radeon1 %{buildroot}/opt/amdgpu/share/licenses/libdrm-amdgpu-radeon1
ln -s /opt/amdgpu/libdrm/share/licenses/libdrm2-amdgpu %{buildroot}/opt/amdgpu/share/licenses/libdrm2-amdgpu
ln -s /opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-common %{buildroot}/opt/amdgpu/share/licenses/libdrm-amdgpu-common
ln -s /opt/amdgpu/libdrm/share/libdrm %{buildroot}/opt/amdgpu/share/libdrm
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf
echo "#/opt/amdgpu/libdrm/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf

%files
"/etc/ld.so.conf.d/libdrm-pro-%{_arch}.conf"
"/opt/amdgpu/libdrm/%{_lib}/*drm*"
"/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-amdgpu1/LICENSE"
"/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-radeon1/LICENSE"
"/opt/amdgpu/libdrm/share/licenses/libdrm2-amdgpu/LICENSE"
"/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-common/LICENSE"
"/opt/amdgpu/libdrm/share/libdrm/amdgpu.ids"
"/opt/amdgpu/share/*"
>>>>>>> bfb7e56 (update 64 to latest release)

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
