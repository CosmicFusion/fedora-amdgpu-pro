Name:     amdamf-pro-runtime
Version:  22.10.2
Release:  1%{?dist}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       System runtime for AMD Advanced Media Framework
URL:      http://repo.radeon.com/amdgpu
Source0: amdamf-pro-runtime-22.10.2.f36.x86_64.tar.gz

Provides:      amf-runtime = 22.10.2-1.fc36
Provides:      amf-runtime(x86-64) = 2.10.2-1.fc36
Provides:      amf-amdgpu-pro = 0:1.4.24-1411481.el9
Provides:      amf-amdgpu-pro(x86-64) = 0:1.4.24-1411481.el9
Provides:      libamfrt64.so.1()(64bit) 
Provides:      libamdenc-amdgpu-pro = 0:1.0-1411481.el9
Provides:      libamdenc-amdgpu-pro(x86-64) = 0:1.0-1411481.el9
Provides:      libamdenc64.so.1.0()(64bit)  
Provides:      libamdenc64.so.1.0()(64bit)  

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      vulkan-amdgpu-pro  

Recommends:	 rocm-opencl-runtime  


%install
tar -xf %{SOURCE0}
mv opt %{buildroot}/
mv usr %{buildroot}/
mv etc %{buildroot}/

%description
Amd encode library

%files
"/etc/ld.so.conf.d/amf-runtime-x86_64.conf"
"/opt/amdgpu-pro/amf/lib64/libamdenc64.so"
"/opt/amdgpu-pro/amf/lib64/libamdenc64.so.1.0"
"/opt/amdgpu-pro/amf/lib64/libamfrt64.so"
"/opt/amdgpu-pro/amf/lib64/libamfrt64.so.1"
"/opt/amdgpu-pro/amf/lib64/libamfrt64.so.1.4.24"
"/opt/amdgpu-pro/share/licenses/amf-amdgpu-pro/AMDGPUPROEULA"
"/opt/amdgpu-pro/share/licenses/libamdenc-amdgpu-pro/AMDGPUPROEULA"
"/usr/lib/.build-id/64/8703809828be73a60bdc89ce14d30b0dbe6ec3"
"/usr/lib/.build-id/66/684e7fad996008265d49313badde8e7609c7ef"

%post -p /sbin/ldconfig



%postun -p /sbin/ldconfig
