# pulls release info from versions file

. ./versions

#

echo "making final tarball"
cd ./debs/extract
tar -czvf ../../../../../amdvlk-pro-rdna2-"$major"."$fedora".i686.tar.gz .


