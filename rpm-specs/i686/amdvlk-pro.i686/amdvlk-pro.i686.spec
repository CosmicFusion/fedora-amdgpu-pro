Name:     amdvlk-pro
Version:  22.10.2
Release:  1%{?dist}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu
Source0:	amdvlk-pro-22.10.2.f36.i686.tar.gz
Provides:      config(amdvlk-pro) = 22.10.2-1.fc36
Provides:      amdvlk-pro = 22.10.2-1.fc36
Provides:      amdvlk-pro(i686) = 22.10.2-1.fc36
Provides:      config(vulkan-amdgpu-pro) = 0:22.10.2-1411481.el9
Provides:      vulkan-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      vulkan-amdgpu-pro(i686) = 0:22.10.2-1411481.el9
Requires:      vulkan-loader

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Recommends:	 openssl-libs  

%install
tar -xf %{SOURCE0}
mv opt %{buildroot}/
mv etc %{buildroot}/

%description
Amdgpu Pro Vulkan driver

%files
"/etc/ld.so.conf.d/amdvlk-pro-i686.conf"
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"
"/opt/amdgpu-pro/vulkan/lib32/amdvlk32.so"

%post 
/sbin/ldconfig 
/usr/bin/ln -s /opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json /usr/share/vulkan/icd.d/amd_pro_icd32.json



%postun -p /sbin/ldconfig
