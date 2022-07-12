# pulls release info from versions file

. ./versions
#

echo "making final tarball"
cd ./debs/extract
tar -czvf ../../../../../amdvlk-"$amdvlk".f36.i686.tar.gz .


