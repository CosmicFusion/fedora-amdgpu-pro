Name:     amdogl-pro
Version:  22.10.2
Release:  2%{?dist}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
URL:      http://repo.radeon.com/amdgpu
Source0:       amdogl-pro-22.10.2.f36.i686.tar.gz
Summary:       AMD OpenGL

Provides:      libEGL.so.1()  
Provides:      libegl-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      libegl-amdgpu-pro(i686) = 0:22.10.2-1411481.el9
Provides:      libglapi-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      libglapi-amdgpu-pro(i686) = 0:22.10.2-1411481.el9
Provides:      libglapi.so.1()  
Provides:      libGLESv2.so.2()  
Provides:      libgles-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      libgles-amdgpu-pro(i686) = 0:22.10.2-1411481.el9
Provides:      config(libgl-amdgpu-pro) = 0:22.10.2-1411481.el9
Provides:      libGL.so.1()  
Provides:      libGLX_amd.so.0()  
Provides:      libgl-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro(i686) = 0:22.10.2-1411481.el9
Provides:      config(libgl-amdgpu-pro-appprofiles) = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-appprofiles = 0:22.10.2-1411481.el9
Provides:      config(libgl-amdgpu-pro-dri) = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-dri = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-dri(i686) = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-ext = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-ext(i686) = 0:22.10.2-1411481.el9


Requires:      libEGL.so.1()    
Requires:      libGLESv2.so.2() 
Requires:      config(libgl-amdgpu-pro) = 0:22.10.2-1411481.el9
Requires:      libGLX_amd.so.0()
Requires:      config(libgl-amdgpu-pro-appprofiles) = 0:22.10.2-1411481.el9
Requires:      config(libgl-amdgpu-pro-dri) = 0:22.10.2-1411481.el9
Requires:      libGL.so.1  
Requires:      libX11-xcb.so.1  
Requires:      libX11.so.6  
Requires:      libXdamage.so.1  
Requires:      libXext.so.6  
Requires:      libXfixes.so.3  
Requires:      libXxf86vm.so.1  
Requires:      libdrm.so.2  
Requires:      libm.so.6
Requires:      libpthread.so.0  
Requires:      libpthread.so.0  
Requires:      libxcb-dri2.so.0  
Requires:      libxcb-glx.so.0  
Requires:      libxcb.so.1  

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

%install
tar -xf %{SOURCE0}
mv opt %{buildroot}/
mv etc %{buildroot}/

%description
Amdgpu Pro OpenGL driver

%files
%attr(0644, root, root) "/etc/ld.so.conf.d/amdogl-pro-i686.conf"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib/dri/amdgpu_dri.so"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib/libEGL.so"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib/libEGL.so.1"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib/libGLESv2.so"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib/libGLESv2.so.2"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib/libglapi.so"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib/libglapi.so.1"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib/xorg/modules/extensions/libglx.so"

%post -p /sbin/ldconfig



%postun -p /sbin/ldconfig
