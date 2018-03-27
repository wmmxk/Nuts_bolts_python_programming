from thread_demo import *
import numpy as np
X = -1 + 2*np.random.rand(10000000) 
Y = c_array_f_multi(X)
print("Y 0:", Y[0])
