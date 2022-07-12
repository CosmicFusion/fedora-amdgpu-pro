# pulls release info from versions file

. ./versions

#

echo "extracting packages"

mkdir ./debs/extract

cd ./debs/extract

ar -x ../vulkan-amdgpu-pro_"$major"-"$minor"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

rm -r ./usr
