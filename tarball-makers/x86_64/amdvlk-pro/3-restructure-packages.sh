# pulls release info from versions file

. ./versions

#

echo "restructuring package directories  "

cd ./rpms/extract

mkdir -p ./opt/amdgpu-pro/vulkan

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/vulkan/
#

echo "fixing .icds "

sed -i "s#/opt/amdgpu-pro/lib64/amdvlk64.so#/opt/amdgpu-pro/vulkan/lib64/amdvlk64.so#" "./opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json"

# 

echo "adding library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdvlk-pro-x86_64.conf

echo "/opt/amdgpu-pro/vulkan/lib64" > ./etc/ld.so.conf.d/amdvlk-pro-x86_64.conf



