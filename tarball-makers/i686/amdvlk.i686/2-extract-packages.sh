# pulls release info from versions file

. ./versions

#

echo "extracting packages"

mkdir ./debs/extract

cd ./debs/extract

ar -x ../amdvlk_"$amdvlk"_i386.deb

tar -xf data.tar.gz

rm -r *.tar*

rm debian-binary
