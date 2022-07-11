# please define the major , minor & rhel version of the packages you want 

major=22.10.2
minor=1411481
rhel_major=9.0
rhel_minor=9

#

echo "extracting packages"

mkdir ./rpms/extract

cd ./rpms/extract

rpm2cpio ../vulkan-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv
