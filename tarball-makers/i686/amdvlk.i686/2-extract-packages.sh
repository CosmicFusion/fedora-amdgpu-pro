# please provide a version

ver=2022.Q2.3

#

echo "extracting packages"

mkdir ./debs/extract

cd ./debs/extract

ar -x ../amdvlk_"$ver"_i386.deb

tar -xf data.tar.gz

rm -r *.tar*

rm debian-binary
