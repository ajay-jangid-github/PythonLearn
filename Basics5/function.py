# functions- it is used to perform a specific task, it is a block of code that only runs when it is called.
# A function can take parameters and return a value. Functions are defined using the def keyword. 

#  define function

def my_func():
  print("hello python")

# my_func()

#  function with parameters . Keyword Arguments
def my_func(age,name):
  # print(f"u r age is , {age}, Name: {name}")
  # print(f"u r age is , {age}")
  # print(f"u r name is , {name}")
  print(f"age :{age}")
  print(f"name : {name}")

my_func(age=26, name="pyhton")
# my_func("python programming")

# return 
# def add(a, b):
#   return a+b

# result = add(20 + 30)
# print("sum is" , result)

# default argument -- value not provide , when function call - then used default value

def default_value(name = "user"):
  print(f"hello , {name}")

default_value()
default_value("Python")

#  Variable-Length Arguments (*args - tuple and **kwargs- dictionary)- when we dont know the , how many  numbers of args will be passed

# def my_sum(*add):
#   return sum(add)

# print(my_sum(10,20,30))
def details(**info):
  for key, value in info.items():
    print(f"{key}:{value}")

details(name = "john" , age = 30, city = "new york")

# lamda function: help of lamda, we can write code in one line- this is the short(binam) function

def add(a,b):
  return a+b

add_lamda = lambda a,b: a + b

print(add(2,3))