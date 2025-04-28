
import csv

with open("employee.csv", mode = 'w', newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(['EmployeeID', 'Age', 'Salary', 'Experience'])
    writer.writerow(['1', 25, '45000', 2])
    writer.writerow(['2', 2, '4000', 4])
    writer.writerow(['3', 15, '60000', 3])
    writer.writerow(['4', 35, '70000', 5])
    writer.writerow(['5', 45, '55000', 1])
    writer.writerow(['6', 65, '35000', 6])
    writer.writerow(['7', 75, '14000', 2])
    writer.writerow(['8', 95, '10000', 5])
    writer.writerow(['9', 85, '46000', 3])
    writer.writerow(['10', 5, '45000', 8])
    


