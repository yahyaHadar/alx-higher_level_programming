#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            pass
        else:
            printed_num += 1
    print()
    return printed_num
