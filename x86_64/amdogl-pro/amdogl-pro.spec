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
Source0:  http://repo.radeon.com/amdgpu/$amdpro/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libegl1-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-dri_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source2:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-ext_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source3:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-glx_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source4:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libglapi1-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source5:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgles2-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source6:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/a/appprofiles-amdgpu-pro/libgl1-amdgpu-pro-appprofiles_%{major}-%{minor}~%{ubuntu}_all.deb

Provides:      libEGL.so.1()(64bit)  
Provides:      libegl-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libegl-amdgpu-pro(x86-64) = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi-amdgpu-pro(x86-64) = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi.so.1()(64bit)  
Provides:      libGLESv2.so.2()(64bit)  
Provides:      libgles-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libgles-amdgpu-pro(x86-64) = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro) = %{major}-%{minor}~%{ubuntu}
Provides:      libGL.so.1()(64bit)  
Provides:      libGLX_amd.so.0()(64bit)  
Provides:      libgl-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro(x86-64) = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro-appprofiles) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-appprofiles = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro-dri) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-dri = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-dri(x86-64) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-ext = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-ext(x86-64) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-glx = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-glx(x86-64) = %{major}-%{minor}~%{ubuntu}

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

Requires:      libdrm-pro  

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Recommends: amdgpu-opengl-switcher

%description
Amdgpu Pro OpenGL driver
