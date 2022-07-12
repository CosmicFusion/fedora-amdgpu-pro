# pulls release info from versions file

. ./versions

#

echo "extracting packages"

mkdir ./rpms/extract

cd ./rpms/extract


rpm2cpio ../libegl-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv

rpm2cpio ../libgl-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv

rpm2cpio ../libgl-amdgpu-pro-appprofiles-"$major"-"$minor".el"$rhel_minor".noarch.rpm | cpio -idmv

rpm2cpio ../libgl-amdgpu-pro-dri-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv

rpm2cpio ../libgl-amdgpu-pro-ext-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv

rpm2cpio ../libglapi-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv

rpm2cpio ../libgles-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv
