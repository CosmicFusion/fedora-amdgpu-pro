# please define the major , minor & ubuntu version of the packages you want 

major=22.10.2
minor=1411481
ubuntu=focal

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
