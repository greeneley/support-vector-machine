
# Review data MNIST

def get_images(img_file, number):
    f = open(img_file, 'rb') # rb: open file in binary mode
    f.read(16) # skip 16 bytes header
    images = []

    for i in range(number):
        image = []
        
        for i in range(28*28):
            image.append(ord(f.read(1))) # ord return the unicode for one-string character

        images.append(image)
    return images

def get_labels(label_file, number):
    l = open(label_file, "rb") # similar above
    l.read(8)
    labels = []
    for i in range(number):
        labels.append(ord(l.read(1)))
    return labels

# number in 2 functions get_images and get_labels is how many datas we'd like to get from file binary

import os
import numpy as np 
from skimage import io # io: read and write image in various formats


def convert_png(images, labels, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    
    for i in range(len(images)):
        out = os.path.join(directory,"%06d-num%d.png"%(i,labels[i]))
        io.imsave(out, np.array(images[i]).reshape(28, 28))


# TEST

# number = 200
train_images = get_images("./train-images-idx3-ubyte", number)
train_labels = get_labels('./train-labels-idx1-ubyte', number)
# convert_png(train_images, train_labels, "previewexe")

# END TEST

def output_csv(images, labels, out_file):
    o = open(out_file, "w")
    for i in range(len(images)):
        o.write(",".join(str(x) for x in [labels[i]] + images[i]) + "\n")
    o.close()


