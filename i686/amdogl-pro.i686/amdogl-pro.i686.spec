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
%global fedora fc36
%global ubuntu 22.04

Name:     amdogl-pro
Version:  	   %{repo}
Release:       4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
URL:      http://repo.radeon.com/amdgpu

Summary:       AMD OpenGL

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libegl1-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_i386.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-dri_%{major}-%{minor}~%{ubuntu}_i386.deb
Source2:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-ext_%{major}-%{minor}~%{ubuntu}_i386.deb
Source3:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-glx_%{major}-%{minor}~%{ubuntu}_i386.deb
Source4:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libglapi1-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_i386.deb
Source5:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgles2-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_i386.deb

Provides:      libEGL.so.1()(64bit)  
Provides:      libegl-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libegl-amdgpu-pro(i686) = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi-amdgpu-pro(i686) = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi.so.1()(64bit)  
Provides:      libGLESv2.so.2()(64bit)  
Provides:      libgles-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libgles-amdgpu-pro(i686) = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro) = %{major}-%{minor}~%{ubuntu}
Provides:      libGL.so.1()(64bit)  
Provides:      libGLX_amd.so.0()(64bit)  
Provides:      libgl-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro(i686) = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro-appprofiles) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-appprofiles = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro-dri) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-dri = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-dri(i686) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-ext = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-ext(i686) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-glx = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-glx(i686) = %{major}-%{minor}~%{ubuntu}

BuildRequires: wget 
BuildRequires: cpio

Requires:      libEGL.so.1()(64bit)    
Requires:      libGLESv2.so.2()(64bit) 
Requires:      config(libgl-amdgpu-pro) = %{major}-%{minor}~%{ubuntu}
Requires:      libGLX_amd.so.0()(64bit)
Requires:      config(libgl-amdgpu-pro-appprofiles) = %{major}-%{minor}~%{ubuntu}
Requires:      config(libgl-amdgpu-pro-dri) = %{major}-%{minor}~%{ubuntu}
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

Requires:      libdrm-pro(i686) 

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Recommends: amdgpu-opengl-switcher(x86_64)

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

%install
mkdir -p %{buildroot}/opt/amdgpu/share/drirc.d
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/dri
#
cp -r files/opt/amdgpu-pro/lib/i386-linux-gnu/* %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/
cp -r files/opt/amdgpu-pro/lib/xorg/modules/extensions/* %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/
cp -r files/usr/lib/i386-linux-gnu/dri/* %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/dri
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdogl-pro-%{_arch}.conf
echo "#/opt/amdgpu-pro/opengl/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdogl-pro-%{_arch}.conf

%files
"/etc/ld.so.conf.d/amdogl-pro-%{_arch}.conf"
"/opt/amdgpu-pro/opengl/%{_lib}/dri/amdgpu_dri.so"
"/opt/amdgpu-pro/opengl/%{_lib}/libEGL*"
"/opt/amdgpu-pro/opengl/%{_lib}/libGL*"
"/opt/amdgpu-pro/opengl/%{_lib}/libgl*"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
