# Percentile -> Quantile-> divide the dataset in to equally parts

import numpy as np

a  = np.array([1000, 2000, 3000, 4000])

pernctile1 = np.percentile(a , 25) # but with help of this- we can find 50-mean, 25th, 75th value
pernctile2 = np.percentile(a, 75)
# mean_value  = np.mean(a) // we can find only mean value

print(pernctile1)
print(pernctile2)
# print(mean_value)

# differnence b/w 2 and 1 ,IQR- (interquartile Range)
iqr = pernctile2 - pernctile1
print("difference b/w p1 and p2 :", iqr)