# pulls release info from versions file

. ./versions

#

echo "extracting packages"

mkdir ./rpms/extract

cd ./rpms/extract

rpm2cpio ../opencl-legacy-amdgpu-pro-icd-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv

rpm2cpio ../ocl-icd-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm | cpio -idmv
