# read a file and print its content

# basic example of reading a file in Python
file = open("my_file.txt", "r")
content = file.read()
file.close()
# print(content)

# using with statement to automatically close the file
with open("my_file.txt", "r") as file:
    content  = file.read()
    print(content)
