# please define the major , minor & ubuntu version of the packages you want 

major=22.10.2
minor=1411481
ubuntu=focal

#

echo "restructuring package directories  "

cd ./debs/extract

mkdir ./opt/amdgpu-pro/vulkan

mv ./opt/amdgpu-pro/lib/i386-linux-gnu ./opt/amdgpu-pro/vulkan/lib32

rm -r ./opt/amdgpu-pro/lib

#

echo "fixing .icds "

sed -i "s#/opt/amdgpu-pro/lib/i386-linux-gnu/amdvlk32.so#/opt/amdgpu-pro/vulkan/lib32/amdvlk32.so#" "./opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json"

# 

echo "adding library path"

mkdir ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdvlk-pro-i686.conf

echo "/opt/amdgpu-pro/vulkan/lib32" > ./etc/ld.so.conf.d/amdvlk-pro-i686.conf
