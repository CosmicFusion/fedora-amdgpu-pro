# pulls release info from versions file

. ./versions

#
cd ./rpms/extract

#

echo "adapting to a mesa friendly environment"

mv ./etc/amd ./etc/amd.bak

rm ./etc/ld.so.conf.d/10-amdgpu-pro-x86_64.conf

mv ./opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf ./opt/amdgpu/share/drirc.d/10-amdgpu-pro.conf.disabled


#

echo "restructuring package directories  "

mkdir -p ./opt/amdgpu-pro/OpenGL

mv ./opt/amdgpu-pro/lib64 ./opt/amdgpu-pro/OpenGL/

mv ./usr/lib64/* ./opt/amdgpu-pro/OpenGL/lib64

rm -r ./usr/lib64

mv ./opt/amdgpu-pro/lib/* ./opt/amdgpu-pro/OpenGL/lib64/

# 

echo "adding *Disabled* library path"

mkdir -p ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdogl-pro-x86_64.conf

echo "# /opt/amdgpu-pro/OpenGL/lib64" > ./etc/ld.so.conf.d/amdogl-pro-x86_64.conf



