# please define the major , minor & ubuntu version of the packages you want 

major=22.10.2
minor=1411481
ubuntu=focal

#

echo "extracting packages"

mkdir ./debs/extract

cd ./debs/extract

####

ar -x ../libegl1-amdgpu-pro_"$major"-"$minor"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libgl1-amdgpu-pro-dri_"$major"-"$minor"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libgl1-amdgpu-pro-ext_"$major"-"$minor"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libglapi1-amdgpu-pro_"$major"-"$minor"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####

ar -x ../libgles2-amdgpu-pro_"$major"-"$minor"_i386.deb

tar -xf data.tar.xz

rm -r *.tar*

rm debian-binary

####










