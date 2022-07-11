Name:          amdvlk
Version:       2022.Q2.3
Release:       1
License:       MIT 
Group:         System Environment/Libraries
Summary:       AMD Open Source Driver for Vulkan

URL:           https://github.com/GPUOpen-Drivers/AMDVLK
Vendor:        Advanced Micro Devices (AMD)

Provides:      amdvlk = 2022.Q2.3-1
Provides:      amdvlk(i686) = 2022.Q2.3-1
Provides:      config(amdvlk) = 2022.Q2.3-1
Requires:      config(amdvlk) = 2022.Q2.3-1
Requires:      vulkan-loader

%install
tar -xf amdvlk-2022.Q2.3.f36.i686.tar.gz
mv usr %{buildroot}/
mv etc %{buildroot}/

%files
"/etc/vulkan/icd.d/amd_icd32.json"
"/etc/vulkan/implicit_layer.d/amd_icd32.json"
"/usr/lib/amdvlk32.so"


%description
AMD Open Source Driver for Vulkan




