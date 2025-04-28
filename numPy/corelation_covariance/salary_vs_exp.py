
import numpy as np

salary = np.array([50000, 40000, 20000,10000])
experience  = np.array([1,2,3,4])

# corealtion - relationship between two variable,like strength and direction-positive & negative
corelation = np.corrcoef(salary, experience)
print(corelation)

# covariance --> magnitude of two variable- like, +(positive) infinte and -(negative)infinite
covariance = np.cov(salary , experience)
print(covariance)