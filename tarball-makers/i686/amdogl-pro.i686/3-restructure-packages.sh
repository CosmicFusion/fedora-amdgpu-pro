# please define the major , minor & ubuntu version of the packages you want 

major=22.10.2
minor=1411481
ubuntu=focal

#
cd ./debs/extract

#

echo "adapting to a mesa friendly environment"

rm -r ./opt/amdgpu


#

echo "restructuring package directories  "

mkdir ./opt/amdgpu-pro/OpenGL

mkdir ./opt/amdgpu-pro/OpenGL/lib

mv ./opt/amdgpu-pro/lib/i386-linux-gnu/* ./opt/amdgpu-pro/OpenGL/lib/

rm -r ./opt/amdgpu-pro/lib/i386-linux-gnu

mv ./usr/lib/i386-linux-gnu/* ./opt/amdgpu-pro/OpenGL/lib/

rm -r ./usr/lib/i386-linux-gnu

mv ./opt/amdgpu-pro/lib/* ./opt/amdgpu-pro/OpenGL/lib

rm -r ./opt/amdgpu-pro/lib

rm -r ./usr

# 

echo "adding *Disabled* library path"

mkdir ./etc

mkdir ./etc/ld.so.conf.d

touch ./etc/ld.so.conf.d/amdogl-pro-i686.conf

echo "# /opt/amdgpu-pro/OpenGL/lib" > ./etc/ld.so.conf.d/amdogl-pro-i686.conf



