import csv 

with open('example.csv', mode = 'r', newline= '') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)