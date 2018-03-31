import multiprocessing as mp
from scipy import random, linalg
import numpy as np
import sys

size = int(sys.argv[1]) # the size of the symmetric matrix
num = int(sys.argv[2]) # compute the inverse num times

#create a symmetric matrix
A = random.rand(size,size)
B = np.dot(A,A.transpose())
print("B[0][0]", B[0][0])

# Define an output queue
output = mp.Queue()

#define the function for compute the inverse of a matrix
def compute_inv(B,i, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    output.put((i,B[0][0]))
    #output.put((i,np.linalg.inv(B)))

# Setup a list of processes that we want to run
processes = [mp.Process(target=compute_inv, args=(B,i, output)) for i in range(num)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]
print("results",results[0])
