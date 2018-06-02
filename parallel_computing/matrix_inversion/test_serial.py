from scipy import random, linalg
import numpy as np
import sys

size = int(sys.argv[1])
num = int(sys.argv[2])
A = random.rand(size,size)
B = np.dot(A,A.transpose())

for i in range(num):
    C = np.linalg.inv(B)
print("inv shape:", C.shape)

