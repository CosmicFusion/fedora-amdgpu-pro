# please define the major , minor & ubuntu version of the packages you want 

major=22.10.2
minor=1411481
ubuntu=focal

#

echo "restructuring package directories  "

cd ./debs/extract

mkdir -p ./opt/amdgpu-pro/OpenCL

mv ./opt/amdgpu-pro/lib/i386-linux-gnu ./opt/amdgpu-pro/OpenCL/lib32

rm -r ./opt/amdgpu-pro/lib

# 

echo "adding library path"

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdocl-legacy-i686.conf

echo "/opt/amdgpu-pro/OpenCL/lib32" > ./etc/ld.so.conf.d/amdocl-legacy-i686.conf
