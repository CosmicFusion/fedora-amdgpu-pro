# please define the major , minor & fedora version of the packages you want 

major=22.10.2
minor=1411481
fedora=f36

#

echo "making final tarball"
cd ./rpms/extract
tar -czvf amf-runtime-"$major"."$fedora".x86_64.tar.gz ./
mv amf-runtime-"$major"."$fedora".x86_64.tar.gz ../../


