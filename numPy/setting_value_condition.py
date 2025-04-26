#  change the elements of an array based on condition

import numpy as np 

a = np.array([10,20,30,40,50])

condition = a[a > 30] = 90
print(a)