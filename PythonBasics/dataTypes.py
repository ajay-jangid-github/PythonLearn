# var can store data in different types-  built-in data types
# like text, Numeric, sequence, Mapping, set types, boolean, Binary, None type
# Text = str 
# Numeric = int float, complex
# Sequence = list, tuple, range
# Mapping = dict
# Set Types = set, frozenset
# Boolean = bool
# Binary Types = byte, bytearray, memoryview
# None Type = NoneType

# complex 
x = 1j
# print(x)
#  tuples
x = ("x1","x2","x3")
# print(x)
# print(type(x))
# range --
x = range(6)
print(x)

# diff- tuple vs dict = (tuple) , {dict}-> {"name":"john", "age": 34}
# dictionary 
x = {'name':'john' , 'age': 32}
# print(x)
# set
x = {"name","age","location"}

# frozendSet

x = frozenset({"name","age","location"})
# print(x)

# memoryView
x = memoryview(bytes(5))
print(x)