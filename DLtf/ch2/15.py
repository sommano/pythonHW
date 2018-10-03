import numpy as np
import tensorflow as tf
import datetime

log_device_placement = True

n = 10
A = np.random.rand(10000, 10000).astype('float32')
B = np.random.rand(10000, 10000).astype('float32')
