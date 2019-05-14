
from mnist import MNIST
# import numpy as np
# from sklearn import svm, metrics

# mndata = MNIST('./mnist')
# train_images, train_labels = mndata.load_training()
# test_images, test_labels = mndata.load_testing()

# 1. Feature scaling

## Viec chuan hoa du lieu 1 buoc quan trong 
## Vi data co the den tu nhieu nguon khac nhau nen co su chenh lech rat lon trong data

train_images = numpy.array(train_images)/255


