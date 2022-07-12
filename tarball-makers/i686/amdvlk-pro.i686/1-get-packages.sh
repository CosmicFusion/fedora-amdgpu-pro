# please define the major , minor & ubuntu version of the packages you want 

major=22.10.2
minor=1411481
ubuntu=focal

#

echo "pulling required packages off repo.radeon.com"

mkdir ./debs

cd ./debs

wget http://repo.radeon.com/amdgpu/"$major"/ubuntu/pool/proprietary/v/vulkan-amdgpu-pro/vulkan-amdgpu-pro_"$major"-"$minor"_i386.deb   
