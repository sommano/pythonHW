import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
#Plot function
def plotresult(org_vec,noisy_vec,out_vec):
 plt.matshow(np.reshape(org_vec, (28, 28)),\
 cmap=plt.get_cmap('gray'))
 plt.title("Original Image")
 plt.colorbar()
 plt.matshow(np.reshape(noisy_vec, (28, 28)),\
 cmap=plt.get_cmap('gray'))
 plt.title("Input Image")
 plt.colorbar()
 outimg = np.reshape(out_vec, (28, 28))\
 plt.matshow(outimg, cmap=plt.get_cmap('gray'))
 plt.title("Reconstructed Image")
 plt.colorbar()
 plt.show()
