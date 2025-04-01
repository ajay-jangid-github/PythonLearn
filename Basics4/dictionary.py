# dictionary -- it is store data in key-value pair
# it is mutable data structure
# it is unordered collection of items

student = {
  "name": "john",
  "age": 20,
  "isActive": True,
  "marks": [90, 80, 70],
  "address" : {
    "city": "new york",
    "state": "NY",
    "country": "USA",
  }
}

# print(student) # print the dictionary
print(student.keys()) # print the keys of the dictionary
print(student.values()) # print the values of the dictionary
print(student.items()) # print the items of the dictionary
print(student.get("name")) # print the value of the key "name"
student["name"] = "Jogn doe"
print(student["name"]) # print the updated value of the key "name"