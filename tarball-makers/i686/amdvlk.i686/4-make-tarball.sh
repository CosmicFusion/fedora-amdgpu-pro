# please provide a version

ver=2022.Q2.3

#

echo "making final tarball"
cd ./debs/extract
tar -czvf amdvlk-"$ver".f36.i686.tar.gz ./
mv amdvlk-"$ver".f36.i686.tar.gz ../../


