import csv 

with open('example2.csv' , mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['hello', 24, 'india'])