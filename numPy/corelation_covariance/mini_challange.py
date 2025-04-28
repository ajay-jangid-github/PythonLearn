
import numpy as np


height = np.array([150, 160, 165, 170, 175, 180])
weight = np.array([50, 55, 60, 65, 70, 80])


corelaton = np.corrcoef(height , weight)
print(corelaton)

covariance = np.cov(height , weight)
print(covariance)