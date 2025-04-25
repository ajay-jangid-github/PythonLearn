# run multiple Thread in one process

import threading

# def print_numbers():
#     for i in range(5):
#         print(i)

# t1 = threading.Thread(target=print_numbers)
# t1.start()
# t1.join()

# def greet():
#   my_list = [1,2,3,4,5]
#   print(my_list)

# list1 = threading.Thread(target=greet)
# list1.start()
# list1.join()

# how to check Thread Through -> ID and Name

def print_number():
  for i in range(5):
    print(f"Thread {threading.current_thread().name} (ID : {threading.get_ident()})-> {i}")


# create Thread
t1 = threading.Thread(target=print_number, name="My Thread")

t1.start()
t1.join()