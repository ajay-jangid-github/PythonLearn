# call function as an argument -- in python function also use as an object
# Aapke code me None print hone ka reason yeh hai ki greet function kuch return nahi kar raha hai. Python me agar koi function explicitly return statement nahi deta, toh woh None return karta hai by default.

# Aapka call_func function func(arg) ka result return kar raha hai, aur func ke jagah greet function pass kiya gaya hai. greet function sirf print karta hai, lekin kuch return nahi karta, isliye call_func ke return value None hoti hai.

# Solution:
# Agar aapko greet function ka output call_func ke through print karwana hai, toh aapko greet function ko modify karna hoga aur usme ek return statement add karna hoga.

# Yeh code modify karke dekhiye:

# Output:
# Ab greet function ek string return karega, jo call_func ke through print ho jayega.



def greet(name):
  # print(f"hello , {name}")
  return f"hello , {name}"

def call_func(func, arg):
  return func(arg)

print(call_func(greet, "john"))