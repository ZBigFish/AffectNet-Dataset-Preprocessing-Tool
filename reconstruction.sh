rm -rf 'AffectNet_class'
mkdir "AffectNet_class"
cd "AffectNet_class"
mkdir "test"
mkdir "train"
cd test
for (( i = 0; i < 8; i++ )); do
    mkdir $i
done
ls
cd ../train
for (( i = 0; i < 8; i++ )); do
    mkdir $i
done
ls
echo "reconstruction complete"