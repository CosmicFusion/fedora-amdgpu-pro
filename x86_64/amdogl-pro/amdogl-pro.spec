%define _build_id_links none

# global info
%global repo 5.5.3
%global major 23.10
%global minor 1620044
# pkg info
%global amf 1.4.30
%global enc 1.0
%global amdvlk 2023.Q3.1
# drm info
%global drm 2.4.114.50503-1620033
%global amdgpu 1.0.0.50503-1636786
# firmware info
%global firmware_rev 6.0.5
%global firmware_maj 50503
%global firmware_min 1620033
%global _firmwarepath	/usr/lib/firmware
# Distro info
%global fedora 38
%global ubuntu 22.04


Name:     amdogl-pro
Version:  	   %{repo}
Release:       4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
URL:      http://repo.radeon.com/amdgpu

Summary:       AMD OpenGL

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/oglp-amdgpu-pro/libegl1-amdgpu-pro-oglp_%{major}-%{minor}.%{ubuntu}_amd64.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/oglp-amdgpu-pro/libgl1-amdgpu-pro-oglp-dri_%{major}-%{minor}.%{ubuntu}_amd64.deb
Source2:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/oglp-amdgpu-pro/libgl1-amdgpu-pro-oglp-ext_%{major}-%{minor}.%{ubuntu}_amd64.deb
Source3:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/oglp-amdgpu-pro/libgl1-amdgpu-pro-oglp-gbm_%{major}-%{minor}.%{ubuntu}_amd64.deb
Source4:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/oglp-amdgpu-pro/libgl1-amdgpu-pro-oglp-glx_%{major}-%{minor}.%{ubuntu}_amd64.deb
Source5:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/oglp-amdgpu-pro/libgles1-amdgpu-pro-oglp_%{major}-%{minor}.%{ubuntu}_amd64.deb
Source6:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/oglp-amdgpu-pro/libgles2-amdgpu-pro-oglp_%{major}-%{minor}.%{ubuntu}_amd64.deb

Provides:      libEGL.so.1()(64bit)  
Provides:      libegl-amdgpu-pro = %{major}-%{minor}.%{ubuntu}
Provides:      libegl-amdgpu-pro(x86_64) = %{major}-%{minor}.%{ubuntu}
Provides:      libglapi-amdgpu-pro = %{major}-%{minor}.%{ubuntu}
Provides:      libglapi-amdgpu-pro(x86_64) = %{major}-%{minor}.%{ubuntu}
Provides:      libglapi.so.1()(64bit)  
Provides:      libGLESv2.so.2()(64bit)  
Provides:      libgles-amdgpu-pro = %{major}-%{minor}.%{ubuntu}
Provides:      libgles-amdgpu-pro(x86_64) = %{major}-%{minor}.%{ubuntu}
Provides:      config(libgl-amdgpu-pro) = %{major}-%{minor}.%{ubuntu}
Provides:      libGL.so.1()(64bit)  
Provides:      libGLX_amd.so.0()(64bit)  
Provides:      libgl-amdgpu-pro = %{major}-%{minor}.%{ubuntu}
Provides:      libgl-amdgpu-pro(x86_64) = %{major}-%{minor}.%{ubuntu}
Provides:      config(libgl-amdgpu-pro-appprofiles) = %{major}-%{minor}.%{ubuntu}
Provides:      libgl-amdgpu-pro-appprofiles = %{major}-%{minor}.%{ubuntu}
Provides:      config(libgl-amdgpu-pro-dri) = %{major}-%{minor}.%{ubuntu}
Provides:      libgl-amdgpu-pro-dri = %{major}-%{minor}.%{ubuntu}
Provides:      libgl-amdgpu-pro-dri(x86_64) = %{major}-%{minor}.%{ubuntu}
Provides:      libgl-amdgpu-pro-ext = %{major}-%{minor}.%{ubuntu}
Provides:      libgl-amdgpu-pro-ext(x86_64) = %{major}-%{minor}.%{ubuntu}
Provides:      libgl-amdgpu-pro-glx = %{major}-%{minor}.%{ubuntu}
Provides:      libgl-amdgpu-pro-glx(x86_64) = %{major}-%{minor}.%{ubuntu}

BuildRequires: wget 
BuildRequires: cpio

Requires:      libEGL.so.1()(64bit)    
Requires:      libGLESv2.so.2()(64bit) 
Requires:      config(libgl-amdgpu-pro) = %{major}-%{minor}.%{ubuntu}
Requires:      libGLX_amd.so.0()(64bit)
Requires:      config(libgl-amdgpu-pro-appprofiles) = %{major}-%{minor}.%{ubuntu}
Requires:      config(libgl-amdgpu-pro-dri) = %{major}-%{minor}.%{ubuntu}
Requires:      libGL.so.1()(64bit)  
Requires:      libX11-xcb.so.1()(64bit)  
Requires:      libX11.so.6()(64bit)  
Requires:      libXdamage.so.1()(64bit)  
Requires:      libXext.so.6()(64bit)  
Requires:      libXfixes.so.3()(64bit)  
Requires:      libXxf86vm.so.1()(64bit)  
Requires:      libdrm.so.2()(64bit)  
Requires:      libm.so.6()(64bit)  
Requires:      libpthread.so.0()(64bit)  
Requires:      libpthread.so.0(GLIBC_2.2.5)(64bit)  
Requires:      libxcb-dri2.so.0()(64bit)  
Requires:      libxcb-glx.so.0()(64bit)  
Requires:      libxcb.so.1()(64bit)  

Requires:      libdrm-pro  

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Recommends: amdgpu-opengl-switcher

%description
Amdgpu Pro OpenGL driver

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

ar x --output . %{SOURCE4}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE5}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE6}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/opt/amdgpu/share/drirc.d
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/dri
#
cp -r files/opt/amdgpu-pro/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/
cp -r files/opt/amdgpu/lib/x86_64-linux-gnu/dri/* %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/dri
cp -r files/opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf %{buildroot}/opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf.disabled
#

%files
"/opt/amdgpu-pro/opengl/%{_lib}/dri/amdgpu_dri.so"
"/opt/amdgpu-pro/opengl/%{_lib}/*"
"/opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf.disabled"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

