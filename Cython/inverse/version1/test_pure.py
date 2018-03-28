from scipy import random, linalg
import numpy as np
import sys

num = int(sys.argv[1])
size = num
A = random.rand(size,size)
B = np.dot(A,A.transpose())

C = np.linalg.inv(B)
print("inv shape:", C.shape)

