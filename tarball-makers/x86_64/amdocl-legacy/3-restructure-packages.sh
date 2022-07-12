# pulls release info from versions file

. ./versions

#

echo "restructuring package directories  "

cd ./rpms/extract

mkdir -p ./opt/amdgpu-pro/OpenCL

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/OpenCL/

# 

echo "adding library path"

mkdir -p ./etc

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdocl-legacy-x86_64.conf

echo "/opt/amdgpu-pro/OpenCL/lib64" > ./etc/ld.so.conf.d/amdocl-legacy-x86_64.conf



