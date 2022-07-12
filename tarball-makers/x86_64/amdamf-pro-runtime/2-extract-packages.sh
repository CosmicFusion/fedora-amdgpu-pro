# please define the major , minor & rhel version of the packages you want 

major=22.10.2
minor=1411481
amf=1.4.24
enc=1.0
rhel_major=9.0
rhel_minor=9

#

echo "extracting packages"

mkdir ./rpms/extract

cd ./rpms/extract

rpm2cpio ../amf-amdgpu-pro-"$amf"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv

rpm2cpio ../libamdenc-amdgpu-pro-"$enc"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv
