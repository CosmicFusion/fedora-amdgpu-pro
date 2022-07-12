Name:     amdogl-pro
Version:  22.10.2
Release:  1%{?dist}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
URL:      http://repo.radeon.com/amdgpu

Summary:       AMD OpenGL

Source0:	amdogl-pro-22.10.2.f36.x86_64.tar.gz
Provides:      libEGL.so.1()(64bit)  
Provides:      libegl-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      libegl-amdgpu-pro(x86-64) = 0:22.10.2-1411481.el9
Provides:      libglapi-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      libglapi-amdgpu-pro(x86-64) = 0:22.10.2-1411481.el9
Provides:      libglapi.so.1()(64bit)  
Provides:      libGLESv2.so.2()(64bit)  
Provides:      libgles-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      libgles-amdgpu-pro(x86-64) = 0:22.10.2-1411481.el9
Provides:      config(libgl-amdgpu-pro) = 0:22.10.2-1411481.el9
Provides:      libGL.so.1()(64bit)  
Provides:      libGLX_amd.so.0()(64bit)  
Provides:      libgl-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro(x86-64) = 0:22.10.2-1411481.el9
Provides:      config(libgl-amdgpu-pro-appprofiles) = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-appprofiles = 0:22.10.2-1411481.el9
Provides:      config(libgl-amdgpu-pro-dri) = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-dri = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-dri(x86-64) = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-ext = 0:22.10.2-1411481.el9
Provides:      libgl-amdgpu-pro-ext(x86-64) = 0:22.10.2-1411481.el9


Requires:      libEGL.so.1()(64bit)    
Requires:      libGLESv2.so.2()(64bit) 
Requires:      config(libgl-amdgpu-pro) = 0:22.10.2-1411481.el9
Requires:      libGLX_amd.so.0()(64bit)
Requires:      config(libgl-amdgpu-pro-appprofiles) = 0:22.10.2-1411481.el9
Requires:      config(libgl-amdgpu-pro-dri) = 0:22.10.2-1411481.el9
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

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Recommends: amdgpu-opengl-switcher

%install
tar -xf %{SOURCE0}
mv opt %{buildroot}/
mv usr %{buildroot}/
mv etc %{buildroot}/

%description
Amdgpu Pro OpenGL driver

%files
%attr(0644, root, root) "/etc/amd.bak/amdapfxx.blb"
%attr(0644, root, root) "/etc/amd.bak/amdrc"
%attr(0644, root, root) "/etc/ld.so.conf.d/amdogl-pro-x86_64.conf"
%attr(0755, root, root) "/opt/amdgpu-pro/OpenGL/lib64/xorg/modules/extensions/libglx.so"
%attr(0755, root, root) "/opt/amdgpu-pro/OpenGL/lib64/dri/amdgpu_dri.so"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libEGL.so"
%attr(0755, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libEGL.so.1"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libGL.so"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libGL.so.1"
%attr(0755, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libGL.so.1.2"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libGLESv2.so"
%attr(0755, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libGLESv2.so.2"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libGLX_amd.so"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libGLX_amd.so.0"
%attr(0755, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libGLX_amd.so.0.0"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libglapi.so"
%attr(0755, root, root) "/opt/amdgpu-pro/OpenGL/lib64/libglapi.so.1"
%attr(0644, root, root) "/opt/amdgpu-pro/share/licenses/libegl-amdgpu-pro/AMDGPUPROEULA"
%attr(0644, root, root) "/opt/amdgpu-pro/share/licenses/libgl-amdgpu-pro-appprofiles/AMDGPUPROEULA"
%attr(0644, root, root) "/opt/amdgpu-pro/share/licenses/libgl-amdgpu-pro-dri/AMDGPUPROEULA"
%attr(0644, root, root) "/opt/amdgpu-pro/share/licenses/libgl-amdgpu-pro-ext/AMDGPUPROEULA"
%attr(0644, root, root) "/opt/amdgpu-pro/share/licenses/libgl-amdgpu-pro/AMDGPUPROEULA"
%attr(0644, root, root) "/opt/amdgpu-pro/share/licenses/libglapi-amdgpu-pro/AMDGPUPROEULA"
%attr(0644, root, root) "/opt/amdgpu-pro/share/licenses/libgles-amdgpu-pro/AMDGPUPROEULA"
%attr(0644, root, root) "/opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf.disabled"


%post -p /sbin/ldconfig



%postun -p /sbin/ldconfig
