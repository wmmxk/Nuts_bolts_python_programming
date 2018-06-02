from scipy import random, linalg
import numpy as np
import sys
import multiprocessing as mp

size = int(sys.argv[1])
num = int(sys.argv[2])
A = random.rand(size,size)
B = np.dot(A,A.transpose())
Bs = [B for i in range(num)]

def compute_inv(B):
    return np.linalg.inv(B)

pool = mp.Pool(processes=2)

results = pool.map(compute_inv, Bs)
print("inv shape:", results[0].shape)

