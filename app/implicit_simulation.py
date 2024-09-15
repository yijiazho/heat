import numpy as np
from matplotlib import pyplot

from utility.thomas import ThomasAlgorithm
   
A = np.array(
    [[6, 2, 0, 0, 0], 
     [2, 4, 1, 0, 0], 
     [0, 1, 7, 2, 0], 
     [0, 0, 2, 4, 1],
     [0, 0, 0, 4, 4]],
    dtype=float)
b = np.array([2, -3, 11, -5, 4], dtype=float)

    
x = ThomasAlgorithm.thomas(A, b)
print (x)
print(np.matmul(A, x))