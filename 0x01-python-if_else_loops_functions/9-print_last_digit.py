#!/usr/bin/python3
def print_last_digit(nbr):
    nbr = abs(nbr)
    last_digt = nbr % 10
    print(last_digt, end='')
    return last_digt
