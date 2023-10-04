#!/usr/bin/python3
def uppercase(str):
    results = ""
    for c in str:
        if 'a' <= c <= ord'z':
            uppercase_c = chr(ord(c) - (ord('a') - ord('A')))
            results += uppercase_c
        else:
            results += c


    if len(results) > 0:
        print("{}".format(results))
