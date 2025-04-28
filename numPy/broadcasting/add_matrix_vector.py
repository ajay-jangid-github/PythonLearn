# broadcasting means--> when array size is not match and shape, then broadcasting help to make same shape and do operation.

import numpy as np 

matrix = np.array([[1,2,3], [4,5,6]])

vector = np.array([10,20,30])

# add matrix and vector
print(matrix + vector)