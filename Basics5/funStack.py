# function stack--> means when we called the function - work on LIFO(last in first out)
# Iska real-world use: Function Execution Control, Recursion, Memory Management.

def first_func():
  print("Start A")
  second_func()
  print("End A")

def second_func():
  print("Start B")
  third_myfunc()
  print("End B")

def third_myfunc():
  print("Inside c")

first_func()