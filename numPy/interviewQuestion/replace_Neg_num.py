  # How would you replace all negative numbers with 0 in a NumPy array?

import numpy as np

a = np.array([1,-1,2,-2,3,-4])

a[a < 0] = 0

print(a)