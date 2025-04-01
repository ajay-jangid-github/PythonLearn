# set -- it  is an unordered collection of unique elements. and not allows duplicates
# #  set is a collection of items, stored multiple values in a single variable

my_set = {1, 2, 3, 4, 5}
# print(my_set) # set with multiple elements
# duplicates
duplicate_set = {6,7,1,1,6}
print(duplicate_set) # set with duplicates

my_tuple = (1, 2, 3, 4, 5,5)
# print(my_tuple) # tuple with duplicates

# union -- it is used to combine two sets

set1  = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) # union of two sets
print(union_set) # union of two sets