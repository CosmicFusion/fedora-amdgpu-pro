# pulls release info from versions file

. ./versions

#

echo "restructuring package directories  "

cd ./debs/extract

mkdir -p ./opt/amdgpu-pro/vulkan-rdna2

mv ./opt/amdgpu-pro/lib/i386-linux-gnu ./opt/amdgpu-pro/vulkan-rdna2/lib32

rm -r ./opt/amdgpu-pro/lib

#

echo "fixing .icds "

sed -i "s#/opt/amdgpu-pro/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu-pro/vulkan-rdna2/lib32/amdvlk32.so#" "./opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"

# 

echo "adding library path"

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdvlk-pro-rdna2-i686.conf

echo "/opt/amdgpu-pro/vulkan-rdna2/lib32" > ./etc/ld.so.conf.d/amdvlk-pro-rdna2-i686.conf
