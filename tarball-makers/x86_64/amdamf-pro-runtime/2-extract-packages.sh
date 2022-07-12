# pulls release info from versions file

. ./versions

#

echo "extracting packages"

mkdir ./rpms/extract

cd ./rpms/extract

rpm2cpio ../amf-amdgpu-pro-"$amf"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv

rpm2cpio ../libamdenc-amdgpu-pro-"$enc"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv
