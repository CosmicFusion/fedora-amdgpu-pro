# please define the major , minor & ubuntu version of the packages you want 

major=22.10.2
minor=1411481
ubuntu=focal

#

echo "pulling required packages off repo.radeon.com"

mkdir ./debs

cd ./debs

wget http://repo.radeon.com/amdgpu/"$major"/ubuntu/pool/proprietary/o/opencl-legacy-amdgpu-pro/opencl-legacy-amdgpu-pro-icd_"$major"-"$minor"_i386.deb  

wget http://repo.radeon.com/amdgpu/"$major"/ubuntu/pool/proprietary/o/ocl-icd-amdgpu-pro/ocl-icd-libopencl1-amdgpu-pro_"$major"-"$minor"_i386.deb 
