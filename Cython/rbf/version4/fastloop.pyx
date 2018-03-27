#cython: boundscheck=False, wraparound=False, nonecheck=False
from libc.math cimport exp as c_exp
import numpy as np
from cython.parallel import prange

def rbf_network_multithread(double[:, :] X,  double[:] beta, double theta):

    cdef int N = X.shape[0]
    cdef int D = X.shape[1]
    cdef double[:] Y = np.zeros(N)
    cdef int i, j, d
    cdef double r = 0

    for i in prange(N, nogil=True):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d])**2 
            r = r**0.5
            Y[i] += beta[j] * c_exp(-(r * theta)**2)

    return Y
