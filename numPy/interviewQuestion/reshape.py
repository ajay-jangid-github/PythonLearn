# mandatory condition -- no. of element will be same

import numpy as np

a = np.arange(9)
a.reshape(3,3)
a.reshape(1,9)
a.reshape(9,1)
# a.reshape(3,4)
print(a)