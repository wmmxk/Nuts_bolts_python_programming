import numpy as np
import sys
import multiply
repeat = int(sys.argv[1])

a = np.arange(120000, dtype=np.float64).reshape((300,400))

print(a[1,1])

multiply.multiply_mul(a, 1.00001,repeat)

print(a[1,1])
