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

Name:     amdogl-pro
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
URL:      http://repo.radeon.com/amdgpu

Summary:       AMD OpenGL

Provides:      libEGL.so.1()(64bit)  
Provides:      libegl-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libegl-amdgpu-pro(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libglapi-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libglapi-amdgpu-pro(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libglapi.so.1()(64bit)  
Provides:      libGLESv2.so.2()(64bit)  
Provides:      libgles-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgles-amdgpu-pro(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      config(libgl-amdgpu-pro) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libGL.so.1()(64bit)  
Provides:      libGLX_amd.so.0()(64bit)  
Provides:      libgl-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      config(libgl-amdgpu-pro-appprofiles) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-appprofiles = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      config(libgl-amdgpu-pro-dri) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-dri = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-dri(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-ext = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-ext(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-glx = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-glx(x86-64) = 0:%{major}-%{minor}.el%{rhel_minor}

Requires:      libEGL.so.1()(64bit)    
Requires:      libGLESv2.so.2()(64bit) 
Requires:      config(libgl-amdgpu-pro) = 0:%{major}-%{minor}.el%{rhel_minor}
Requires:      libGLX_amd.so.0()(64bit)
Requires:      config(libgl-amdgpu-pro-appprofiles) = 0:%{major}-%{minor}.el%{rhel_minor}
Requires:      config(libgl-amdgpu-pro-dri) = 0:%{major}-%{minor}.el%{rhel_minor}
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

BuildRequires: wget 
BuildRequires: cpio

Recommends: amdgpu-opengl-switcher

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/rpms

cd %{buildroot}/rpms

wget http://repo.radeon.com/amdgpu/"%{amdpro}/rhel/"%{rhel_major}/proprietary/x86_64/libegl-amdgpu-pro-"%{major}-"%{minor}.el"%{rhel_minor}".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"%{amdpro}/rhel/"%{rhel_major}/proprietary/x86_64/libgl-amdgpu-pro-"%{major}-"%{minor}.el"%{rhel_minor}".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"%{amdpro}/rhel/"%{rhel_major}/proprietary/x86_64/libgl-amdgpu-pro-appprofiles-"%{major}-"%{minor}.el"%{rhel_minor}".noarch.rpm

wget http://repo.radeon.com/amdgpu/"%{amdpro}/rhel/"%{rhel_major}/proprietary/x86_64/libgl-amdgpu-pro-dri-"%{major}-"%{minor}.el"%{rhel_minor}".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"%{amdpro}/rhel/"%{rhel_major}/proprietary/x86_64/libgl-amdgpu-pro-ext-"%{major}-"%{minor}.el"%{rhel_minor}".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"%{amdpro}/rhel/"%{rhel_major}/proprietary/x86_64/libglapi-amdgpu-pro-"%{major}-"%{minor}.el"%{rhel_minor}".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"%{amdpro}/rhel/"%{rhel_major}/proprietary/x86_64/libgles-amdgpu-pro-"%{major}-"%{minor}.el"%{rhel_minor}".x86_64.rpm

###

echo "extracting packages"

mkdir -p %{buildroot}/rpms/extract

cd %{buildroot}/rpms/extract

rpm2cpio ../libegl-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

rpm2cpio ../libgl-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

rpm2cpio ../libgl-amdgpu-pro-appprofiles-"%{major}"-"%{minor}".el"%{rhel_minor}".noarch.rpm | cpio -idmv

rpm2cpio ../libgl-amdgpu-pro-dri-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

rpm2cpio ../libgl-amdgpu-pro-ext-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm  | cpio -idmv

rpm2cpio ../libglapi-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

rpm2cpio ../libgles-amdgpu-pro-"%{major}"-"%{minor}".el"%{rhel_minor}".x86_64.rpm | cpio -idmv

###

#

echo "restructuring package directories  "

cd  %{buildroot}/rpms/extract

echo "adapting to a mesa friendly environment"

mv ./etc/amd ./etc/amd.bak

rm ./etc/ld.so.conf.d/10-amdgpu-pro-x86_64.conf

mv ./opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf ./opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf.disabled

#

echo "restructuring package directories  "

mkdir -p ./opt/amdgpu-pro/OpenGL

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/OpenGL/

mv ./usr/lib64/* ./opt/amdgpu-pro/OpenGL/lib64

rm -r ./usr/lib64

mv ./opt/amdgpu-pro/lib/* ./opt/amdgpu-pro/OpenGL/lib64/

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu-pro/OpenGL/lib64/*.so

# 



echo "adding *Disabled* library path"

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdogl-pro-x86_64.conf

echo "# /opt/amdgpu-pro/OpenGL/lib64" > ./etc/ld.so.conf.d/amdogl-pro-x86_64.conf



cd %{buildroot}/rpms/extract

mv ./opt %{buildroot}/
mv ./usr %{buildroot}/
mv ./etc %{buildroot}/
rm -r %{buildroot}/usr/lib/.build-id || echo 'no build-ids :)'

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
%exclude "/rpms"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
