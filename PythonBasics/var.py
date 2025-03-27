# no need to specify variable type 
x = 3; #int 
y = "str" #string

# if need data type , when will be use casting

x = int(3)
y = str("str")

# get the data type variable- using type() function

x = 5
y = "john"
z = 0.5

print(type(z))

# single or double quotes- for define string variable

x = "john"
y = 'john'

# case sensitive -- var names are case sensitive
x = "john"
X = 5

# variables - start with _ and letter, not start with number, start with alph-numeric char, and underscores, shoud not py keywords
#multi words var- camel case, pascal case, snake case
# camel case- each words capital, except first word
myVarName = "var"
# pascal case - each words capital
MyVarName = "var"
# snake case - using underscore b/w words
my_var_name = "var"

# Python Variables - Assign Multiple Values

x, y, z  = "value of x", "value of y", "value of z"
# print(x)
# print(y)
# print(z)

# One Value to Multiple Variables
x = y = z = "same value of all"
# print(x)
# print(y)
# print(z)

# Unpack a Collection
laptop_names = ["del","lenovo","hp"]
x, y, z = laptop_names
# print("x:" + "=" + x)
# print("y:" + "=" + y)
# print("z:" + "=" + z)

# output variable 

x, y , z = "del","hp","lenovo"
# print(x, y, z)
# print(x + y + z)

# if we trying string and int value no. it will give error
# x = int("string") not valid 
# y = int(4)
# print(x + y)
# but this will not give error
x = "string"
y = str(4)
# print(x + y)

# Python - Global Variables - means declare variable outside of function & also use everywhere outside and inside of block

# outside var use inside of block func
x = "outside var used inside of function" 

# def myfunc():
#   print("x global: "+ x)

# myfunc()

# same variable name use inside the fun , call only inside locally, and global remain same as 

# x = "outside"

# def myfunc():
#   y = "inside var"
#   # print("Var from inside" + y) // cant access outside

# myfunc()

# print("var form outside" + y) # not print y 

#if we want to access inside func var - use global 

def myfunc():
  global x
  x = "inside var used by global keyword"

myfunc()

print(x)