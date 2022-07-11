# fedora-amdgpu-pro
A repository that provides the proprietary driver for fedora without having to deal with hassle of getting RHEL repo to work , and it has 32 bit libraries.

The end goal of this repository is to hand it over to glourious eggroll , so he can use it to supply AMD proprietary to nobara/fedora users


# Q&A

* Who's responsiable for this?


Some dumb 14 year old on the internet.


* Proprietary drivers on AMD? thought those guys were open source ??


While yes AMD driver stack is mostly open-source , some corporate greed still runs in the blood
as some parts still remains proprietary such as :


- The legacy/pal/orca OpenCL drivers. (required for darktable , resolve & blender (< 3.0) .)
- The industrial OpenGL drivers (required for resolve.)
- The Advanced Media Framework System Runtime 
- A Vulkan driver with ray tracing capabilities
