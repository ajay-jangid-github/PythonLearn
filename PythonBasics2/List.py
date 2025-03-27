#  list- store multiple items in single variable
# list items are ordered changeable and allow duplicate values


mylist = ["item1","item2","item3","item1"]
# print(len(mylist)) check items length

# also any data types 
# string
mylist = ["item1","item2","item3","item1"]
# int
mylist = [1,2,3,4]
# boolean
mylist = [True, False]

# list() Constructor 
mylist = (("del","hp"))
# print(mylist)

# set - changeable, ordederd, and allows duplicate
# tuple = unordered, but unchangeable- but add/remove
# dictionary = ordered but above 3.6 version and no duplicate

# change listItems
thislist = ["del","hp","lenovo"]
thislist[1] = "del"
# print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[2:5] = "papaya","apple","mango"
# print(thislist)

# insert Items = without changing and replace existing items - using insert() method

myNewList = ["l1","l2","l3","l4","l5"]
myNewList.insert(5,"list6")
# print(myNewList)

# add items at the end , use append

myNewList = ["l1","l2","l3","l4","l5"]
myNewList.append("lsit7")
# print(myNewList)

# Extend List
myNewList = ["l1","l2","l3","l4","l5"]
mySecondList = ["list"]
myNewList.extend(mySecondList)
print(myNewList)