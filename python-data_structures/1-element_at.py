#!/usr/bin/python3

def element_at(my_list, idx):
    index = my_list[idx]
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return "Element at index {} is {}".format(idx, my_list[idx])