#  it is also similiar to list but it is immutable (unchangeable) data structure
# #  tuple is a collection of items, stored multiple values in a single variable
my_tuple = (1,2,3,4,5)
# print(my_tuple)

# single element tuple
my_single_element_tuple = (1,) # tuple with single element 
print(my_single_element_tuple) # tuple with single element

# tuple indexing and slicing

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1]) # accessing the second element of the tuple
print(my_tuple[-1]) # accessing the last element of the tuple
print(my_tuple[1:3]) # accessing the second and third elements of the tuple
print(my_tuple[:3]) # accessing the first three elements of the tuple
print(my_tuple[1:]) # accessing the second to last elements of the tuple
print(my_tuple[::2]) # accessing every second element of the tuple
print(my_tuple[::-1]) # reversing the tuple
