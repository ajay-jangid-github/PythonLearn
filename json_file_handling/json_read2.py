import json


with open('data2.json', mode = "r" , newline= '') as file:
    data = json.load(file)
    print(data)
    print(data["age"])