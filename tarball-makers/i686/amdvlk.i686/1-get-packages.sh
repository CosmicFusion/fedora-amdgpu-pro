# pulls release info from versions file

. ./versions
#

echo "pulling required packages off repo.radeon.com"

mkdir ./debs

cd ./debs

wget http://repo.radeon.com/amdvlk/apt/debian/pool/main/a/amdvlk/amdvlk_"$amdvlk"_i386.deb
