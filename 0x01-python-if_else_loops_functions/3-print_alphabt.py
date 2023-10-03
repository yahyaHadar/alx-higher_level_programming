#!/usr/bin/python3

for e in range(ord('a'), ord('z') + 1):
     if e != ord('e') and e != ord('q'):
         print("{:e}".format(e), end="")
