# fedora-amdgpu-pro
This repository contains scripts for repacking the AMD proprietary drivers into Fedora-usable packages. It includes both 64 and 32 bit drivers.

# Q&A

* Proprietary drivers on AMD? thought those guys were open source ??

AMD's proprietary drivers only support a few linux distributions: Ubuntu, OpenSUSE, RHEL, CentOS. Other distributions have to repackage their drivers.

While yes AMD driver stack is mostly open-source , as some parts remains proprietary like :

- The legacy/pal/orca OpenCL drivers. (required for darktable , resolve & blender (< 3.0) .)
- The industrial OpenGL drivers (required for resolve.)
- The Advanced Media Framework (required for GPU H.264/H.265 encoding)
- Vulkan drivers with ray tracing capabilities

# How to build the packages:

**"**IMPORTANT BUILD NOTES**"** : 

1) Occasionally, the mock build may fail on 32 bit packages with the following issue:
```
Failed:
  shadow-utils-2:4.11.1-2.fc36.i686                                                                                                                                                                                                                               

Error: Transaction failed
```
This is a known issue. You can just ignore it and re-run the build.  

2) It seems like AMD maintainers forgot enable rdna2 AMF encoding support in amdvlk-pro starting from amdgpu-pro 21.50 and onwards , so please use **amdvlk-pro-rdna2** if you have a rdna2 GPU. (6000 series or higher):  
https://github.com/GPUOpen-LibrariesAndSDKs/AMF/issues/334


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
amdamf-pro-runtime
amdocl-legacy
amdogl-pro
amdvlk
amdvlk-pro
amdvlk-pro-rdna2
-------------------------------------
32 bit package names are:
amdocl-legacy
amdogl-pro
amdvlk
amdvlk-pro
amdvlk-pro-rdna2
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

- The system will do what it needs to do automatically .


