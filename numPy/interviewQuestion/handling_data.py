# so if the data is missing- use nanmean(), nanstd() etc.

import numpy as np 

# a = np.array([100, 300, np.nan, 450])

# mean_value = np.nanmean(a) # ignore NAN
# std_value = np.nanstd(a)

# print(mean_value)
# print(std_value)

# a = np.mean(np.array([[1,2],[3,4]]), axis=0)
a = np.mean(np.array([[1,2], [3,4]]), axis = 0)
# mean_value = np.mean(a)
print(a)