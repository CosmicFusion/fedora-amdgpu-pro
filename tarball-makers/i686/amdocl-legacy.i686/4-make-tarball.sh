# please define the major , minor & fedora version of the packages you want 

major=22.10.2
minor=1411481
fedora=f36

#

echo "making final tarball"
cd ./debs/extract
tar -czvf amdocl-legacy-"$major"."$fedora".i686.tar.gz ./
mv amdocl-legacy-"$major"."$fedora".i686.tar.gz ../../


