if [ ! -f "AffectNet_class" ]; then
    mkdir "AffectNet_class"
fi
cd "AffectNet_class"
if [ -f "test" ]; then
    rm -rf "test"
fi
if [ -f "train" ]; then
    rm -rf "train"
fi
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
echo "create file folder complete"
python "affectnet_preprocess.py"