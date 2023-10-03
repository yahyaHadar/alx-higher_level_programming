#!/usr/bin/python3
def remove_char_at(str, n):
    newstrr = ""
    for i, c in enumerate(str):
        if i != n:
            newstrr += c
        return newstrr
