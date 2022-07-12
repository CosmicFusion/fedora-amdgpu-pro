Name:     amdvlk-pro
Version:  22.10.2
Release:  2%{?dist}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD Vulkan
URL:      http://repo.radeon.com/amdgpu
Source: amdvlk-pro-22.10.2.f36.x86_64.tar.gz

Provides:      config(amdvlk-pro) = 22.10.2-1.fc36
Provides:      amdvlk-pro = 22.10.2-1.fc36
Provides:      amdvlk-pro(x86-64) = 22.10.2-1.fc36
Provides:      config(vulkan-amdgpu-pro) = 0:22.10.2-1411481.el9
Provides:      vulkan-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      vulkan-amdgpu-pro(x86-64) = 0:22.10.2-1411481.el9
Requires:      vulkan-loader

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Recommends:	 openssl-libs  
Recommends:	 amdgpu-vulkan-switcher

%install
tar -xf %{SOURCE0}
mv opt %{buildroot}/
mv usr %{buildroot}/
mv etc %{buildroot}/

%description
Amdgpu Pro Vulkan driver

%files
"/opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json"
"/opt/amdgpu-pro/share/licenses/vulkan-amdgpu-pro/AMDGPUPROEULA"
"/opt/amdgpu-pro/vulkan/lib64/amdvlk64.so"
"/usr/lib/.build-id/d8/44d90033815cb1376acbc25d573011b40df7d8"
"/etc/ld.so.conf.d/amdvlk-pro-x86_64.conf"

%post 
/sbin/ldconfig 
/usr/bin/ln -s /opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json /usr/share/vulkan/icd.d/amd_pro_icd64.json



%postun -p /sbin/ldconfig
