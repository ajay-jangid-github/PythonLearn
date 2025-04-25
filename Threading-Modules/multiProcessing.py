# to create different Types of process- for full utilization of cpu
# import multiprocessing

# def print_number():
#   for i in range(5):
#     print(i)

# t1 = multiprocessing.Process(target=print_number)

# t1.start()
# t1.join()

import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

p1 = multiprocessing.Process(target=print_numbers)
p1.start()
p1.join()
