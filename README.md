# Deprecated and Archived!
With recent commits to [VA-API](https://freedesktop.org/wiki/Software/vaapi/) AMD proprietary AMF is virtually useless on AMD hardware except polaris/GFX8/RX 5XX/RX 4XX series, but with AMF depending on the proprietary vulkan driver and that dropping support for Polaris too, it's now actually universally useless.

on top of that the proprietary vulkan driver lost it's RT Edge to [Mesa RADV](https://docs.mesa3d.org/drivers/radv.html) So it's useless too.

The proprietary OpenCL implentation is broken, unsupported, and unusable USE [ROCm](https://www.amd.com/en/products/software/rocm.html).

Meanwhile the much more performant [Mesa radeonSI](https://www.x.org/wiki/RadeonFeature/) is now fully compatible with proprietary applications such as davinci resolve .

# fedora-amdgpu-pro
This repository contains scripts for repacking the AMD proprietary drivers into Fedora-usable packages. It includes both 64 and 32 bit drivers.

# Q&A

* Proprietary drivers on AMD? thought those guys were open source ??

AMD's proprietary drivers only support a few linux distributions: Ubuntu LTS, SLES, RHEL, CentOS. Other distributions have to repackage their drivers.

While yes AMD driver stack is mostly open-source , as some parts remains proprietary like :

- The legacy/pal/orca OpenCL drivers. (required for darktable , resolve & blender (< 3.0) , they also behave better than the ROCm OpenCL implentation when using wine .)
- The industrial OpenGL drivers (required for resolve.)
- The Advanced Media Framework (required for GPU H.264/H.265 encoding)
- Vulkan drivers with ray tracing capabilities

# How to build the packages:

**"**IMPORTANT NOTES**"** : 

1) Occasionally, the mock build may fail on 32 bit packages with the following issue:
```
Failed:
  shadow-utils-2:4.11.1-2.fc36.i686                                                                                                                                                                                                                               

Error: Transaction failed
```
This is a known issue. You can just ignore it and re-run the build.  

2) Starting from amdgpu-pro 21.50 the driver components -MUST- match the version of their firmware, and it's recommended to also match the drm version
    so we have repackaged the official "libdrm" along with the official amdgpu firmware used for their dkms modules, which we re-routed to be used for the amdgpu module in your kernel to fix these issues.

3) We have made these libdrm libraries load using system wrappers (vk_pro, gl_pro, cl_pro)

4) Using the official firmware will not cause any side-effects, they are practically the same as the normal ones except being properly versioned


We include a package builder script which uses mock to build packages with minimal dependencies. It will auto install the dependencies it needs (mock pykickstart fedpkg libvirt)  

Use the package builder to build specific packages:  
```
$ ./package-builder.sh 
-------------------------------------
Usage: <package-name> <architecture>
-------------------------------------
You must specify a package name and an architecture.
Achitecture options are "32" for 32 bit and "64" for 64 bit
-------------------------------------
64 bit package names are:
amd-gpu-pro-firmware
libdrm-pro
amdamf-pro-runtime
amdocl-legacy
amdogl-pro
amdvlk
amdvlk-pro
-------------------------------------
32 bit package names are:
libdrm-pro
amdocl-legacy
amdogl-pro
amdvlk
amdvlk-pro
```

# How to install the packages:

Resulting packages are placed in the "package" subfolder. Install packages like so:
```
$ cd packages
$ sudo dnf install *.rpm
```

# How to use Vulkan PRO drivers:

- install amdgpu-vulkan-switcher from https://copr.fedorainfracloud.org/coprs/gloriouseggroll/amdgpu-vulkan-switcher/
 
- Run the program with 
  
```
vk_pro {THE_PROGRAM}
```
 
# How to use Vulkan AMDVLK drivers:

- install amdgpu-vulkan-switcher from https://copr.fedorainfracloud.org/coprs/gloriouseggroll/amdgpu-vulkan-switcher/

**AMDVLK**
 
- Run the program with 
 
```
vk_amdvlk {THE_PROGRAM}
```

# How to use AMD AMF encoder:

- The only requirement to use the AMF encoder is that it requires the PRO driver to be used, so you must run the application (such as obs or ffmpeg) with vk_pro:

```
vk_pro {THE_PROGRAM}
```

Note : H265 AMF is supported only on RDNA1 cards and higher (RX 5XXX) , the rest shall use H264.

# How to use the OpenGL PRO drivers:

- install amdgpu-opengl-switcher from https://copr.fedorainfracloud.org/coprs/gloriouseggroll/amdgpu-vulkan-switcher/


- Run the program with 
```
gl_pro {THE_PROGRAM}
```

- You can also use  the open source zink driver:

```
gl_zink {THE_PROGRAM}
```

# How to use the OpenCL drivers:

- install amdgpu-opencl-switcher from https://copr.fedorainfracloud.org/coprs/gloriouseggroll/amdgpu-vulkan-switcher/

- Run the program with 
```
cl_pro {THE_PROGRAM}

