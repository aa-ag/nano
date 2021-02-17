# https://realpython.com/python-timer/

###--- imports ---###
import time


######------ O(n^2) ------######

def quad_example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print("Items: {}, {}".format(first_loop_item, second_loop_item))


quad_example([1, 2, 3, 4])
print(time.process_time())
print(time.perf_counter())
