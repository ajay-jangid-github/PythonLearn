# remove list specified items --- remove method
myList = ["list1","list2","list3"]
myList.remove("list2")
# print(myList)

# remove index - use pop() method , if we not specify the index, remove last item 
# also we can use del keyword--- 
myList = ["list1","list2","list3"]
# myList.pop(2)
del myList[2]
# print(myList)

#  clear the list -- we can empty the list
myList = ["list1","list2","list3"]
myList.clear()
print(myList)