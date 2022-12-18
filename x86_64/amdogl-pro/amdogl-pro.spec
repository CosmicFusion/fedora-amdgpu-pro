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
# Distro info
>>>>>>> bfb7e56 (update 64 to latest release)
%global fedora fc36
%global ubuntu 22.04

Name:     amdogl-pro
<<<<<<< HEAD
Version:       %{amdpro}
Release:       3.%{fedora}
License:       AMD GPU PRO EULA 
=======
Version:  	   %{repo}
Release:       4%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
>>>>>>> bfb7e56 (update 64 to latest release)
Group:         System Environment/Libraries
URL:      http://repo.radeon.com/amdgpu

Summary:       AMD OpenGL

<<<<<<< HEAD
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
=======
%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libegl1-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source1:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-dri_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source2:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-ext_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source3:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgl1-amdgpu-pro-glx_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source4:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libglapi1-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source5:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/o/opengl-amdgpu-pro/libgles2-amdgpu-pro_%{major}-%{minor}~%{ubuntu}_amd64.deb
Source6:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/proprietary/a/appprofiles-amdgpu-pro/libgl1-amdgpu-pro-appprofiles_%{major}-%{minor}~%{ubuntu}_all.deb

Provides:      libEGL.so.1()(64bit)  
Provides:      libegl-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libegl-amdgpu-pro(x86_64) = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi-amdgpu-pro(x86_64) = %{major}-%{minor}~%{ubuntu}
Provides:      libglapi.so.1()(64bit)  
Provides:      libGLESv2.so.2()(64bit)  
Provides:      libgles-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libgles-amdgpu-pro(x86_64) = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro) = %{major}-%{minor}~%{ubuntu}
Provides:      libGL.so.1()(64bit)  
Provides:      libGLX_amd.so.0()(64bit)  
Provides:      libgl-amdgpu-pro = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro(x86_64) = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro-appprofiles) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-appprofiles = %{major}-%{minor}~%{ubuntu}
Provides:      config(libgl-amdgpu-pro-dri) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-dri = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-dri(x86_64) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-ext = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-ext(x86_64) = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-glx = %{major}-%{minor}~%{ubuntu}
Provides:      libgl-amdgpu-pro-glx(x86_64) = %{major}-%{minor}~%{ubuntu}

BuildRequires: wget 
BuildRequires: cpio

Requires:      libEGL.so.1()(64bit)    
Requires:      libGLESv2.so.2()(64bit) 
Requires:      config(libgl-amdgpu-pro) = %{major}-%{minor}~%{ubuntu}
Requires:      libGLX_amd.so.0()(64bit)
Requires:      config(libgl-amdgpu-pro-appprofiles) = %{major}-%{minor}~%{ubuntu}
Requires:      config(libgl-amdgpu-pro-dri) = %{major}-%{minor}~%{ubuntu}
>>>>>>> bfb7e56 (update 64 to latest release)
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

<<<<<<< HEAD
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
=======
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
mkdir -p %{buildroot}/etc/amd
mkdir -p %{buildroot}/opt/amdgpu/share/drirc.d
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/dri
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libegl1-amdgpu-pro
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-dri
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-ext
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-glx
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libglapi1-amdgpu-pro
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgles2-amdgpu-pro
mkdir -p %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-appprofiles
#
cp -r files/opt/amdgpu-pro/lib/x86_64-linux-gnu/* %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/
cp -r files/opt/amdgpu-pro/lib/xorg/modules/extensions/* %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/
cp -r files/usr/lib/x86_64-linux-gnu/dri/* %{buildroot}/opt/amdgpu-pro/opengl/%{_lib}/dri
cp -r files/opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf %{buildroot}/opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf.disabled
cp -r files/etc/amd/*  %{buildroot}/etc/amd
#
cp -r files/usr/share/doc/libegl1-amdgpu-pro/copyright %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libegl1-amdgpu-pro/LICENSE
cp -r files/usr/share/doc/libgl1-amdgpu-pro-dri/copyright %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-dri/LICENSE
cp -r files/usr/share/doc/libgl1-amdgpu-pro-ext/copyright %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-ext/LICENSE
cp -r files/usr/share/doc/libgl1-amdgpu-pro-glx/copyright %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-glx/LICENSE
cp -r files/usr/share/doc/libglapi1-amdgpu-pro/copyright %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libglapi1-amdgpu-pro/LICENSE
cp -r files/usr/share/doc/libgles2-amdgpu-pro/copyright %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgles2-amdgpu-pro/LICENSE
cp -r files/usr/share/doc/libgl1-amdgpu-pro-appprofiles/copyright %{buildroot}/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-appprofiles/LICENSE
#
mkdir -p %{buildroot}/opt/amdgpu-pro/share/licenses
ln -s /opt/amdgpu-pro/opengl/share/licenses/libegl1-amdgpu-pro %{buildroot}/opt/amdgpu-pro/share/licenses/libegl1-amdgpu-pro
ln -s /opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-dri %{buildroot}/opt/amdgpu-pro/share/licenses/libgl1-amdgpu-pro-dri
ln -s /opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-ext %{buildroot}/opt/amdgpu-pro/share/licenses/libgl1-amdgpu-pro-ext
ln -s /opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-glx %{buildroot}/opt/amdgpu-pro/share/licenses/libgl1-amdgpu-pro-glx
ln -s /opt/amdgpu-pro/opengl/share/licenses/libglapi1-amdgpu-pro %{buildroot}/opt/amdgpu-pro/share/licenses/libglapi1-amdgpu-pro
ln -s /opt/amdgpu-pro/opengl/share/licenses/libgles2-amdgpu-pro %{buildroot}/opt/amdgpu-pro/share/licenses/libgles2-amdgpu-pro
ln -s /opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-appprofiles %{buildroot}/opt/amdgpu-pro/share/licenses/libgl1-amdgpu-pro-appprofiles
#
echo "adding *Disabled* library path"
mkdir -p %{buildroot}/etc/ld.so.conf.d
touch %{buildroot}/etc/ld.so.conf.d/amdogl-pro-%{_arch}.conf
echo "#/opt/amdgpu-pro/opengl/%{_lib}" > %{buildroot}/etc/ld.so.conf.d/amdogl-pro-%{_arch}.conf

%files
"/etc/amd/amdapfxx.blb"
"/etc/amd/amdrc"
"/etc/ld.so.conf.d/amdogl-pro-%{_arch}.conf"
"/opt/amdgpu-pro/opengl/%{_lib}/dri/amdgpu_dri.so"
"/opt/amdgpu-pro/opengl/%{_lib}/libEGL*"
"/opt/amdgpu-pro/opengl/%{_lib}/libGL*"
"/opt/amdgpu-pro/opengl/%{_lib}/libgl*"
"/opt/amdgpu-pro/opengl/share/licenses/libegl1-amdgpu-pro/LICENSE"
"/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-appprofiles/LICENSE"
"/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-dri/LICENSE"
"/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-ext/LICENSE"
"/opt/amdgpu-pro/opengl/share/licenses/libgl1-amdgpu-pro-glx/LICENSE"
"/opt/amdgpu-pro/opengl/share/licenses/libglapi1-amdgpu-pro/LICENSE"
"/opt/amdgpu-pro/opengl/share/licenses/libgles2-amdgpu-pro/LICENSE"
"/opt/amdgpu-pro/share/*"
"/opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf.disabled"
>>>>>>> bfb7e56 (update 64 to latest release)

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
<<<<<<< HEAD
=======

>>>>>>> bfb7e56 (update 64 to latest release)
