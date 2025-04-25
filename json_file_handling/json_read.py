import json

# def write_json_file(file_path, data):
#     """Writes data to a JSON file."""
#     with open(file_path, 'w') as json_file:
#         json.dump(data, json_file, indent=4)  

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
    # print(type(data))
    print(data["name"])
