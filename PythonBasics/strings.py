# slicing strings - specify start and end index

x = "my slice string"
# print(x[1:4])

b = "Hello, World!"
# print(b[2:])

# modify string
# upper case
x = "hello world"
# print(x.upper())
# print(x.lower())

# reomve whitespaces - strip()

x = "  hello world   "
# print(x.strip())

# replace string - replace()

x = "hello world"
# print(x.replace("hello","HELLO"))

# split string --> split method return a list and split the string into substring

x = "hello , john, what r u doing"
# print(x.split(","))

# string concatenationm - by using + operator
a = "hello"
b = "john"
z = a + " " + b
# print(z)

# string formatting - as i learned we cannot add sting and int, but help of formating we can.

a = "john is"
b = 36
c = 2
add = f"{a}  {b: .2f}" # modifier- put 2 decimal , also math oepration
mul = f"{b * c}"
# print(add)
# print(mul)

# Escape Character - we cannot use double quoute inside , repeat again, but with backslash \

# x = "my name is john "and i am learning python" " # generate error
x = "my name is john \"and i am learning python\" " # right way
# print(x)

# function true and false

def myfunc():
  return 0

print(bool(myfunc()))
