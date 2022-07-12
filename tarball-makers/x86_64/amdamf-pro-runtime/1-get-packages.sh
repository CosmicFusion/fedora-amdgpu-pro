# pulls release info from versions file

. ./versions
#

echo "pulling required packages off repo.radeon.com"

mkdir ./rpms

cd ./rpms

wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/amf-amdgpu-pro-"$amf"-"$minor".el"$rhel_minor".x86_64.rpm
wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/libamdenc-amdgpu-pro-"$enc"-"$minor".el"$rhel_minor".x86_64.rpm
