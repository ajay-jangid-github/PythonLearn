# used to change the shape without changing the data
import numpy as np

a = np.array([1,2,3,4,5,6])
b = a.reshape(-1, 3)
print(b)