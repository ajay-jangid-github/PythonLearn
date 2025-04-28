import numpy as np 

# load the data
data = np.genfromtxt('employee.csv', delimiter= ',', skip_header= 1)

# split columns

employee_id = data[:, 0]
age = data[:,1]
salary = data[:,2]
experience = data[:,3]

# statistical analysis
print("avg salary", np.mean(salary))
print("max salary", np.max(salary))
print("avg salary", np.mean(experience))

# high salary count
high_Salary_count = np.sum(salary > 60000)
print(high_Salary_count)