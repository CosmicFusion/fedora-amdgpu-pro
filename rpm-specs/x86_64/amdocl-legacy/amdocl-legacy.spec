Name:          amdocl-legacy
Version:       22.10.2
Release:       2%{?dist}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD OpenCL ICD Loaders


URL:           http://repo.radeon.com/amdgpu

Source0:	amdocl-legacy-22.10.2.f36.x86_64.tar.gz





Provides:      amdocl-legacy = 22.10.2-1.fc36
Provides:      amdocl-legacy(x86-64) = 22.10.2-1.fc36
Provides:      config(opencl-legacy-amdgpu-pro-icd) = 0:22.10.2-1411481.el9
Provides:      libOpenCL.so.1()(64bit)  
Provides:      libOpenCL.so.1()(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.0)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.0)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.1)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.1)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.2)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_1.2)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.0)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.0)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.1)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.1)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.2)(64bit)  
Provides:      libOpenCL.so.1(OPENCL_2.2)(64bit)  
Provides:      libamdocl-orca64.so()(64bit)  
Provides:      libamdocl-orca64.so()(64bit)  
Provides:      libamdocl-orca64.so(ACL_0.8)(64bit)  
Provides:      libamdocl-orca64.so(ACL_0.8)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.0)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.0)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.1)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.1)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.2)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_1.2)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_2.0)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_2.0)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_2.1)(64bit)  
Provides:      libamdocl-orca64.so(OPENCL_2.1)(64bit)  
Provides:      libopencl-amdgpu-pro = 22.10.2-1411481.el9
Provides:      ocl-icd-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      ocl-icd-amdgpu-pro(x86-64) = 0:22.10.2-1411481.el9
Provides:      opencl-legacy-amdgpu-pro-icd = 0:22.10.2-1411481.el9
Provides:      opencl-legacy-amdgpu-pro-icd(x86-64) = 0:22.10.2-1411481.el9
Provides:      opencl-orca-amdgpu-pro-icd  
Requires(post): /sbin/ldconfig  
Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig  


%install
tar -xf %{SOURCE0}
mv opt %{buildroot}/
mv usr %{buildroot}/
mv etc %{buildroot}/

%description
OpenCL (Open Computing Language) is a multivendor open standard for
general-purpose parallel programming of heterogeneous systems that include
CPUs, GPUs and other processors. + The ICD Loader library provided by AMD.

%files
"/etc/OpenCL/vendors/amdocl-orca64.icd"
"/etc/ld.so.conf.d/amdocl-legacy-x86_64.conf"
"/opt/amdgpu-pro/OpenCL/lib64/libOpenCL.so.1"
"/opt/amdgpu-pro/OpenCL/lib64/libOpenCL.so.1.2"
"/opt/amdgpu-pro/OpenCL/lib64/libamdocl-orca64.so"
"/opt/amdgpu-pro/share/licenses/ocl-icd-amdgpu-pro/AMDGPUPROEULA"
"/opt/amdgpu-pro/share/licenses/opencl-legacy-amdgpu-pro-icd/AMDGPUPROEULA"
"/usr/lib/.build-id/46/765da00a9db985132b93e56c8eaf7f7d2cded8"




%post -p /sbin/ldconfig



%postun -p /sbin/ldconfig

%changelog

