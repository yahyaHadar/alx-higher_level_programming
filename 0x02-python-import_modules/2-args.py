#!/usr/bin/python3
import sys
num = len(sys.argv) -1
def pluralize(num):
    if num == 1:
        return "argument"
    else:
        return "arguments"

print("{} {}:".format(num, pluralize(num)))

for i in range(1, num + 1):
    print("{}: {}".format(i, sys.argv[i]))
