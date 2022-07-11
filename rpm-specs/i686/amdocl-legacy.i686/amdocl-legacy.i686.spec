Name:     amdocl-legacy
Version:  22.10.2
Release:  1%{?dist}
License:       AMD GPU PRO EULA 
Group:         System Environment/Libraries
Summary:       AMD OpenCL ICD Loaders
URL:      http://repo.radeon.com/amdgpu
Source0: http://repo.radeon.com/amdgpu/22.10.2/ubuntu/pool/proprietary/o/opencl-legacy-amdgpu-pro/opencl-legacy-amdgpu-pro-icd_22.10.2-1411481_i386.deb
Source1: http://repo.radeon.com/amdgpu/22.10.2/ubuntu/pool/proprietary/o/ocl-icd-amdgpu-pro/ocl-icd-libopencl1-amdgpu-pro_22.10.2-1411481_i386.deb
Provides:      config(opencl-legacy-amdgpu-pro-icd) = 0:22.10.2-1411481.el9
Provides:      opencl-legacy-amdgpu-pro-icd = 0:22.10.2-1411481.el9
Provides:      opencl-legacy-amdgpu-pro-icd(i686) = 0:22.10.2-1411481.el9
Provides:      opencl-orca-amdgpu-pro-icd  
Provides:      libopencl-amdgpu-pro = 22.10.2-1411481.el9
Provides:      ocl-icd-amdgpu-pro = 0:22.10.2-1411481.el9
Provides:      ocl-icd-amdgpu-pro(i686) = 0:22.10.2-1411481.el9

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

%install
tar -xf amdocl-legacy-22.10.2.f36.i686.tar.gz
mv opt %{buildroot}/
mv etc %{buildroot}/

%description
OpenCL (Open Computing Language) is a multivendor open standard for
general-purpose parallel programming of heterogeneous systems that include
CPUs, GPUs and other processors. + The ICD Loader library provided by AMD.

%files
"/etc/OpenCL/vendors/amdocl-orca32.icd"
"/etc/ld.so.conf.d/amdocl-legacy-i686.conf"
"/opt/amdgpu-pro/OpenCL/lib32/libOpenCL.so.1"
"/opt/amdgpu-pro/OpenCL/lib32/libOpenCL.so.1.2"
"/opt/amdgpu-pro/OpenCL/lib32/libamdocl-orca32.so"

%post -p /sbin/ldconfig



%postun -p /sbin/ldconfig
