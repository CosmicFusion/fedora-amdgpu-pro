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
%global fedora fc36
%global ubuntu 22.04

Name:     libdrm-pro
Version:  %{repo}
Release:  4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       AMD proprietary libdrm
URL:      http://repo.radeon.com/amdgpu

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



BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires: 	libdrm

%description
AMD proprietary libdrm

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz

ar x --output . %{SOURCE2}
tar -xJC files -f data.tar.xz

ar x --output . %{SOURCE3}
tar -xJC files -f data.tar.xz

%install
mkdir -p %{buildroot}/opt/amdgpu/libdrm/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-amdgpu1
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-radeon1
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm2-amdgpu
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-common
mkdir -p %{buildroot}/opt/amdgpu/libdrm/share/libdrm
#
install -p -m755 files/opt/amdgpu/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu/libdrm/%{_lib}/
install -p -m755 files/usr/share/doc/libdrm-amdgpu-amdgpu1/copyright %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-amdgpu1/LICENSE
install -p -m755 files/usr/share/doc/libdrm-amdgpu-radeon1/copyright %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-radeon1/LICENSE
install -p -m755 files/usr/share/doc/libdrm2-amdgpu/copyright %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm2-amdgpu/LICENSE
install -p -m755 files/usr/share/doc/libdrm-amdgpu-common/copyright %{buildroot}/opt/amdgpu/libdrm/share/licenses/libdrm-amdgpu-common/LICENSE
install -p -m755 files/opt/amdgpu/share/libdrm/amdgpu.ids %{buildroot}/opt/amdgpu/libdrm/share/libdrm/amdgpu.ids 
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

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
