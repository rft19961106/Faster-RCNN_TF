import os
import random

trainval_percent = 0.5
train_percent = 0
xmlfilepath = r'E:\2020program\FAST-RCNN\Faster-RCNN-TensorFlow-Python3-master\data\VOCdevkit2007\VOC2007\Annotations'
txtsavepath = r'E:\2020program\FAST-RCNN\Faster-RCNN-TensorFlow-Python3-master\data\VOCdevkit2007\VOC2007\ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(r'E:\2020program\FAST-RCNN\Faster-RCNN-TensorFlow-Python3-master\data\VOCdevkit2007\VOC2007\ImageSets\Main\trainval.txt', 'w')
ftest = open(r'E:\2020program\FAST-RCNN\Faster-RCNN-TensorFlow-Python3-master\data\VOCdevkit2007\VOC2007\ImageSets\Main\test.txt', 'w')
ftrain = open(r'E:\2020program\FAST-RCNN\Faster-RCNN-TensorFlow-Python3-master\data\VOCdevkit2007\VOC2007\ImageSets\Main\train.txt', 'w')
fval = open(r'E:\2020program\FAST-RCNN\Faster-RCNN-TensorFlow-Python3-master\data\VOCdevkit2007\VOC2007\ImageSets\Main\val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()