from fastloop import rbf_network_multithread
import time
import numpy as np
import sys


D = 5
N = 1000
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10
n = int(sys.argv[1])

start = time.clock()
for i in range(n):
    Y = rbf_network_multithread(X,beta,theta)

end = time.clock()

time = (end-start)/n
print ("time taken: ", time)

