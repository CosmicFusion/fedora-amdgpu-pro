# pulls release info from versions file

. ./versions

#

echo "extracting packages"

mkdir ./rpms/extract

cd ./rpms/extract

rpm2cpio ../vulkan-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv
