# fedora-amdgpu-pro
A repository that provides the proprietary driver for fedora without having to deal with hassle of getting RHEL repo to work , and it has 32 bit libraries.

The end goal of this repository is to hand it over to glourious eggroll , so he can use it to supply AMD proprietary to nobara/fedora users


# Q&A

* Who's responsiable for this?


Some dumb 14 year old on the internet.


* Proprietary drivers on AMD? thought those guys were open source ??


While yes AMD driver stack is mostly open-source , some corporate greed still runs in the blood
as some parts remains proprietary like :


- The legacy/pal/orca OpenCL drivers. (required for darktable , resolve & blender (< 3.0) .)
- The industrial OpenGL drivers (required for resolve.)
- The Advanced Media Framework System Runtime 
- A Vulkan driver with ray tracing capabilities


# How to use

- install the binaries from the releases section or maybe a repo one day or learn to generate them on your own system

 **"**WARNING**"** : It seems like AMD maintainers forgot enable rdna2 in amdvlk-pro starting from amdgpu-pro 21.50 and onwards , so please use **amdvlk-pro-rdna2** if you have a rdna2 GPU.

# For Vulkan

- install amdgpu-vulkan-switcher from https://copr.fedorainfracloud.org/coprs/gloriouseggroll/amdgpu-vulkan-switcher/

 **AMDVLK_PRO**
 
 - Run the program with 
  
  ```
  vk_pro {THE_PROGRAM}
   ```
 
 

**AMDVLK**

 **"**WARNING**"** : Since you get the 64 bit amdvlk binary directly from AMD's github you need to symlink their icd so that the amdgpu-vulkan-switcher can read it.
 
 - To do that , run
 ```
sudo ln -s /etc/vulkan/icd.d/amd_icd64.json /usr/share/vulkan/icd.d/amd_icd64.json
   ```
 
 
 - Run the program with 
  
  ```
  vk_amdvlk {THE_PROGRAM}
  ```

# For AMF

- Just run the program the needs AMF with vk_pro and it will work.

# For OpenCL

- The system will do what it needs to do automatically .

# For OpenGL

- install amdgpu-opengl-switcher from https://github.com/CosmicFusion/amdgpu-opengl-switcher


 - And run your program with
```
gl_pro {THE_PROGRAM}
```
- You can also use zink


```
gl_zink {THE_PROGRAM}
```

.

# How to manually compile 

There are a bunch of .spec files in this repository , choose what you want to build and build it the spec using the proper architecture (x86_64 or i686) , and enjoy!
eg : 
# you want "$source"/x86_64/amdvlk-pro , a.k.a 64-bit vulkan amdgpu pro

```
rpmbuild -bb --target=x86_64 "$source"/x86_64/amdvlk-pro/amdvlk-pro.spec
```
# you want "$source"/i686/amdvlk-pro , a.k.a 32-bit vulkan amdgpu pro

```
rpmbuild -bb --target=i686 "$source"/i686/amdvlk-pro/amdvlk-pro.i686.spec
```

 **"**WARNING**"** : This script depends on rpmbuild cleaning to clean the build directory , so if building was for any reason cancelled or failed , do not attempt to build again , until you erase the builddir manually , or else it **"**WILL**"** fail .
.
