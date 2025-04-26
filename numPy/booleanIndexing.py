# Boolean Indexing-- select the array of elements based on condition

import numpy as np

a = np.array([10,20,30,40,50])

# check the multiple condition

condition  = a[(a > 20) & (a < 40)]
condition2 = a[(a == 20) | (a == 40)]
print(condition)
print(condition2)
