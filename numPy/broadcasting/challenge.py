# Matrix ke saath vector ka addition karo (broadcasting use karke).

# Matrix ke har element me 5 add karo (broadcasting style).

import numpy as np

matrix = np.array([[100, 200, 300],
                   [400, 500, 600],
                   [700, 800, 900]])
b = np.array([5])

vector = np.array([1, 2, 3])
# addition matrix and vector

print(matrix + vector)

# add 5 in matrix
print(matrix + b)