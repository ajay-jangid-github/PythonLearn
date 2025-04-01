# identity and Membership operators
#  is,is not -->do variables same memory location par hai ya nhi
# in , not in --> check karte hai ki koi value kisi collection me hai ya nhi

a = [1,2,3]
b = [1,2,3]
# faLSE- not in same memory location
# print(a is b) 
# True- same value
print(a == b)  

text = "Python Programming"
print("jaav" in text)