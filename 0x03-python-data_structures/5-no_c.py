#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_string = ""
    for c in range(len(my_string)):
        if my_string[c] != 'c' and my_string[c] != 'C':
            new_string = new_string + my_string[c]
    return new_string
