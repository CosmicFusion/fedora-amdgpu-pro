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

BuildRequires: wget 
BuildRequires: cpio

Requires:      libdrm-pro  

Provides:      libEGL.so.1()  
Provides:      libegl-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libegl-amdgpu-pro(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libglapi-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libglapi-amdgpu-pro(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libglapi.so.1()  
Provides:      libGLESv2.so.2()  
Provides:      libgles-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgles-amdgpu-pro(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      config(libgl-amdgpu-pro) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libGL.so.1()  
Provides:      libGLX_amd.so.0()  
Provides:      libgl-amdgpu-pro = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      config(libgl-amdgpu-pro-appprofiles) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-appprofiles = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      config(libgl-amdgpu-pro-dri) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-dri = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-dri(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-ext = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-ext(i686) = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-glx = 0:%{major}-%{minor}.el%{rhel_minor}
Provides:      libgl-amdgpu-pro-glx(i686) = 0:%{major}-%{minor}.el%{rhel_minor}

Requires:      libEGL.so.1()    
Requires:      libGLESv2.so.2() 
Requires:      config(libgl-amdgpu-pro) = 0:%{major}-%{minor}.el%{rhel_minor}
Requires:      libGLX_amd.so.0()
Requires:      config(libgl-amdgpu-pro-appprofiles) = 0:%{major}-%{minor}.el%{rhel_minor}
Requires:      config(libgl-amdgpu-pro-dri) = 0:%{major}-%{minor}.el%{rhel_minor}
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

%build

echo "pulling required packages off repo.radeon.com"

mkdir -p %{buildroot}/debs

cd %{buildroot}/debs

wget http://repo.radeon.com/amdgpu/%{amdpro}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libegl1-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

wget http://repo.radeon.com/amdgpu/%{amdpro}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-dri_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

wget http://repo.radeon.com/amdgpu/%{amdpro}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-ext_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

wget http://repo.radeon.com/amdgpu/%{amdpro}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-glx_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

wget http://repo.radeon.com/amdgpu/%{amdpro}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libglapi1-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

wget http://repo.radeon.com/amdgpu/%{amdpro}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgles2-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

###

echo "extracting packages"

mkdir -p %{buildroot}/debs/extract

cd %{buildroot}/debs/extract

####

ar -x ../libegl1-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libgl1-amdgpu-pro-dri_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libgl1-amdgpu-pro-ext_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libgl1-amdgpu-pro-glx_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libglapi1-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libgles2-amdgpu-pro_"%{major}"-"%{minor}"~"%{ubuntu}"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

###

cd %{buildroot}/debs/extract

#

echo "adapting to a mesa friendly environment"

rm -r ./opt/amdgpu

rm -r  ./etc/amd/amdrc

rm -r   ./etc/ld.so.conf.d/10-amdgpu-pro-i386.conf

#

echo "restructuring package directories  "

mkdir -p ./opt/amdgpu-pro/OpenGL

mkdir -p ./opt/amdgpu-pro/OpenGL/lib32

mv ./opt/amdgpu-pro/lib/i386-linux-gnu/* ./opt/amdgpu-pro/OpenGL/lib32/

rm -r ./opt/amdgpu-pro/lib/i386-linux-gnu

mv ./usr/lib/i386-linux-gnu/* ./opt/amdgpu-pro/OpenGL/lib32/

rm -r ./usr/lib/i386-linux-gnu

mv ./opt/amdgpu-pro/lib/* ./opt/amdgpu-pro/OpenGL/lib32

rm -r ./opt/amdgpu-pro/lib

rm -r ./usr

# 

echo 'patching libs to use official libdrm'

sed -i "s|libdrm|libdro|g" ./opt/amdgpu-pro/OpenGL/lib32/*.so


# 

echo "adding *Disabled* library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdogl-pro-i686.conf

echo "# /opt/amdgpu-pro/OpenGL/lib32" > ./etc/ld.so.conf.d/amdogl-pro-i686.conf




###

mv ./opt %{buildroot}/
mv ./etc %{buildroot}/

%description
Amdgpu Pro OpenGL driver

%files
%attr(0644, root, root) "/etc/ld.so.conf.d/amdogl-pro-i686.conf"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib32/dri/amdgpu_dri.so"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib32/libEGL.so"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib32/libEGL.so.1"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib32/libGLESv2.so"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib32/libGLESv2.so.2"
%attr(0777, root, root) "/opt/amdgpu-pro/OpenGL/lib32/libglapi.so"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib32/libglapi.so.1"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib32/xorg/modules/extensions/libglx.so"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib32/libGL*"
%attr(0644, root, root) "/opt/amdgpu-pro/OpenGL/lib32/libGLX_amd*"
%exclude "/debs"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig
