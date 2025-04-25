#  means --> call the outer functionality in inner function, store outer function variable in inner functiona even execute outer function


# why we use closure--
# Encapsulation- protect variable, Memory Efficient- variable store hone ke bad, bar bar use define nhi karna padta hain, Python Decorators - to modify function


def outer_function(msg):
  def inner_function():
    print(f"Message: {msg}")
  return inner_function
  
closure_function = outer_function("Hello ,python")
closure_function()