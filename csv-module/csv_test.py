import csv

filename = f"c:\\Users\\user\Desktop\\pYTHOn-roadmap\\names.csv"

def extract_unique_names(filename):
  unique_names = set()
  with open(filename, mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
      unique_names.add(row[0])
  return unique_names

print(extract_unique_names(filename))