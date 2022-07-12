# pulls release info from versions file

. ./versions

#

echo "extracting packages"

mkdir ./debs/extract

cd ./debs/extract

ar -x ../opencl-legacy-amdgpu-pro-icd_"$major"-"$minor"_i386.deb 

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

rm -r ./usr

ar -x ../ocl-icd-libopencl1-amdgpu-pro_"$major"-"$minor"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

rm -r ./usr
