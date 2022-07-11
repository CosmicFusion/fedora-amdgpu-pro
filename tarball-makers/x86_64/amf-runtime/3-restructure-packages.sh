# please define the major , minor & rhel version of the packages you want 

major=22.10.2
minor=1411481
amf=1.4.24
enc=1.0
rhel_major=9.0
rhel_minor=9

#

echo "restructuring package directories  "

cd ./rpms/extract

mkdir ./opt/amdgpu-pro/amf

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/amf/

# 

echo "adding library path"

mkdir ./etc

mkdir ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amf-runtime-x86_64.conf

echo "/opt/amdgpu-pro/amf/lib64" > ./etc/ld.so.conf.d/amf-runtime-x86_64.conf



