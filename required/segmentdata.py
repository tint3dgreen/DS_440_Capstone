import os
import random

parent = '../volume/data/interim/Cancer_Set'

def fileCount(path):
    return len([name for name in os.listdir(path)])

directories = ['Annotations','ImageSets','JPEGImages']


#Comment these out after first run
os.mkdir(os.path.join(parent,directories[1],'Main'))
os.mkdir(os.path.join(parent,directories[0]))
os.mkdir(os.path.join(parent,directories[1]))
os.mkdir(os.path.join(parent,directories[2]))

path = os.path.join(parent,directories[0])
count = fileCount(path)
data = []
for file in os.listdir(path):
    data.append(file.split(".")[0])
#shuffle the data
random.shuffle(data)

#assign training and validation set
val = data[int(3*len(data)/10):int(6.5*len(data)/10)]
test = data[:3*int(len(data)/10)]
train = data[int(6.5*len(data)/10):]
print(len(train))
print(len(val))
print(len(test))



#write train set
with open("../volume/data/interim/Cancer_Set/ImageSets/Main/train.txt",'w') as f:
    for image in train:
        f.write(image +"\n")
with open("../volume/data/interim/Cancer_Set/ImageSets/Main/tumor_train.txt",'w') as f:
    for image in train:
        f.write(image +" 0"+"\n")

#write val set
with open("../volume/data/interim/Cancer_Set/ImageSets/Main/val.txt",'w') as f:
    for image in val:
        f.write(image +"\n")
with open("../volume/data/interim/Cancer_Set/ImageSets/Main/tumor_val.txt",'w') as f:
    for image in val:
        f.write(image +" 0"+"\n")

#write train_val set
with open("../volume/data/interim/Cancer_Set/ImageSets/Main/trainval.txt",'w') as f:
    for image in val:
        f.write(image +"\n")
    for image in train:
        f.write(image +"\n")
#write train_val set
with open("../volume/data/interim/Cancer_Set/ImageSets/Main/tumor_trainval.txt",'w') as f:
    for image in val:
        f.write(image + " 0"+"\n")
    for image in train:
        f.write(image + " 0"+"\n")

#write test
with open("../volume/data/interim/Cancer_Set/ImageSets/Main/test.txt",'w') as f:
    for image in test:
        f.write(image + "\n")
