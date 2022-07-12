Name:     amdvlk-pro-rdna2
Version:  21.40.2
Release:  2%{?dist}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD Vulkan for rdna2
URL:      http://repo.radeon.com/amdgpu
Source0:	amdvlk-pro-rdna2-21.40.2.f36.i686.tar.gz
Provides:      config(amdvlk-pro) = 21.40.2-1.fc36
Provides:      amdvlk-pro = 21.40.2-1.fc36
Provides:      amdvlk-pro(i686) = 21.40.2-1.fc36
Provides:      config(vulkan-amdgpu-pro) = 0:21.40.2-1350682.el8
Provides:      vulkan-amdgpu-pro = 0:21.40.2-1350682.el8
Provides:      vulkan-amdgpu-pro(i686) = 0:21.40.2-1350682.el8
Requires:      vulkan-loader

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Recommends:	 openssl-libs  

%install
tar -xf %{SOURCE0}
mv opt %{buildroot}/
mv etc %{buildroot}/

%description
Amdgpu Pro Vulkan driver for rdna2

%files
"/etc/ld.so.conf.d/amdvlk-pro-rdna2-i686.conf"
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"
"/opt/amdgpu-pro/vulkan-rdna2/lib32/amdvlk32.so"
"/opt/amdgpu-pro/vulkan-rdna2/lib32/amdvlk32.so.1.0"

%post 
/sbin/ldconfig 
/usr/bin/ln -s /opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json /usr/share/vulkan/icd.d/amd_pro_icd32.json



%postun -p /sbin/ldconfig
