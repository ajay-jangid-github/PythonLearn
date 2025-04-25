
# this code writes data to a csv file using the csv module
# it creates a file called data.csv and writes the data to 
# it in the form of rows and columns
# the first row contains the headers and the rest of the rows contain the data
# the data is written in the form of a list of lists

import csv

with open("data.csv", mode = 'w', newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['ajay', 25, 'jaipur'])
    writer.writerow(['raj', 25, 'delhi'])
    writer.writerow(['raj', 25, 'delhi'])
    