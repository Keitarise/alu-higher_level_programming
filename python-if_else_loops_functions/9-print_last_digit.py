#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    if number <= 0:
        return "{}{}".format(last_digit, last_digit)
    else:
        return last_digit
print(print_last_digit(-98))
