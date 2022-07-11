# please define the major , minor & rhel version of the packages you want 

major=22.10.2
minor=1411481
rhel_major=9.0
rhel_minor=9

#

echo "pulling required packages off repo.radeon.com"

mkdir ./rpms

cd ./rpms

wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/libegl-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/libgl-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/libgl-amdgpu-pro-appprofiles-"$major"-"$minor".el"$rhel_minor".noarch.rpm

wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/libgl-amdgpu-pro-dri-"$major"-"$minor".el"$rhel_minor".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/libgl-amdgpu-pro-ext-"$major"-"$minor".el"$rhel_minor".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/libglapi-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm

wget http://repo.radeon.com/amdgpu/"$major"/rhel/"$rhel_major"/proprietary/x86_64/libgles-amdgpu-pro-"$major"-"$minor".el"$rhel_minor".x86_64.rpm
