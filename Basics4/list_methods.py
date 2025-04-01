# append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy

x = [1, 2, 3, 4, 5]
# x.append(6) # append adds an element to the end of the list
# print(x)
# x.extend([7,9]) # extend adds multiple elements to the end of the list
# # print(x)
# x.insert(0, 5) # insert adds an element at a specific index
# x.insert(2, 6) # insert adds an element at a specific index
# # print(x)

x.remove(5) # remove removes the first occurrence of a value from the list
# print(x)

x.pop() # pop removes the last element from the list and returns it
# print(x)
# print(x.clear()) # clear removes all elements from the list

# append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy

# fruits = ["apple", "banana", "cherry", "date","cherry"]

fruits = [1,3,2,6,5]
# fruits.index("banana") # index returns the index of the first occurrence of a value in the list
# print(fruits.index("banana")) # index returns the index of the first occurrence of a value in the list
# print(fruits.count("cherry")) # count returns the number of occurrences of a value in the list  
fruits.sort()
print(fruits) # sort sorts the list in ascending order

fruits.reverse() # reverse reverses the order of the elements in the list
print(fruits)

fruits2 = fruits.copy() # copy creates a shallow copy of the list 
print(fruits2) # copy creates a shallow copy of the list  