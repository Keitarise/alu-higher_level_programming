#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []  # Create an empty list to store the results
    for item in range(my_list):
        if my_list[i] % 2 == 0:
            results.append("{} is divisible by 2".format(item))
        else:
            results.append("{} is not divisible by 2".format(item))
    return results
