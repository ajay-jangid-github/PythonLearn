
#  here--> how to write data to a json format file in python
# 1. import json module
import json 

data = {
  "name" : "ajay",
  "age" : 23,
  "city" : "jaipur"
}

with open('data2.json', 'w') as json_file:
    # 2. use json.dump() to write data to a file
    json.dump(data, json_file, indent=4) # indent is used for pretty printing
# 3. use json.dumps() to convert data to a json string