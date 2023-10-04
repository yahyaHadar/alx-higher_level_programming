#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            uppercase_c = chr(ord(c) - (ord('a') - ord('A')))
            print(uppercase_c, end='')
        else:
            print(char, end='')

    print()
