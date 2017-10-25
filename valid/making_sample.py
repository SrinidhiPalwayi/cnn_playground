import os
import glob
import numpy as np
from shutil import copyfile

g = glob.glob ('*.jpg')
shuf = np.random.permutation(g) #any random permutation of images

for i in range(100) :
    copyfile(shuf[i], '/Users/nidhi/Desktop/VIP/dogsvscats.bak' + '/sample/valid/' + shuf[i])