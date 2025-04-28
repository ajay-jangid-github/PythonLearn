import numpy as np 

salaries = np.array([3000,4000, 5000, 6000])

# mean salary
mean_salary = np.mean(salaries)
# print(mean_salary)

# std salary
std_salary = np.std(salaries)
# print(std_salary)

# variance - means how much data spread out 
vari_salary = np.var(salaries)
print(vari_salary)

# min & max salary
min_salary  = np.min(salaries)
max_salary = np.max(salaries)
print(min_salary)
print(max_salary)

# sum salary
sum_salary = np.sum(salaries)
print(sum_salary)