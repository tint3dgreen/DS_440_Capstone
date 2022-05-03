# DS_440_Capstone

##Instructions\n
First, run download_data.py in /required to donwload the data

Then run the preprocessing with Preproc_Script.py in src/features

run segmentdata.py in /required

then copy the data folder into the top level of https://github.com/tint3dgreen/faster-rcnn.pytorch-capstone

install dependencies for faster-Rcnn
```
cd lib
python setup.py build develop
cd ..
```
for training
```
python python trainval_net.py --dataset pascal_voc --net vgg16 --bs 1 --nw 2 --lr .004 --lr_decay_step 5 --cuda --epoch 15 --save_dir $SAVEDIR
```
for test
```
python test_net.py --dataset pascal_voc --net vgg16 --checksession $session --checkepoch $epoch --checkpoint $checkpoint --cuda --load_dir $loadDir
```
