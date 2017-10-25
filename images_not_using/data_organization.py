import os
import glob
import numpy as np

g = glob.glob ('cat.*.jpg')
shuf = np.random.permutation(g) #any random permutation of images

for i in range(400) :
    os.rename(shuf[i], '/Users/nidhi/Desktop/VIP/dogsvscats' + '/valid/' + shuf[i])
    #this moved cats from training to train1 so that eventually will not use train



#for i in range(400) :
 #   os.rename(shuf[i], '/Users/nidhi/Desktop/VIP/dogsvscats' + '/valid/' + shuf[i])
    # this moved cats from training to validation


