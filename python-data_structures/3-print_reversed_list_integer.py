#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        my_list.reverse()
        for item in my_list:
            print("{}".format(item))
