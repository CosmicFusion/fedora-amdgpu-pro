#

echo "restructuring package directories  "

cd ./debs/extract

mv ./usr/lib/i386-linux-gnu/* ./usr/lib/

rm -r ./usr/lib/i386-linux-gnu

rm -r ./usr/share

#

echo "fixing .icds "

sed -i "s#/usr/lib/i386-linux-gnu/amdvlk32.so#/usr/lib/amdvlk32.so#" "./etc/vulkan/icd.d/amd_icd32.json"

sed -i "s#/usr/lib/i386-linux-gnu/amdvlk32.so#/usr/lib/amdvlk32.so#" "./etc/vulkan/implicit_layer.d//amd_icd32.json"
