#!/usr/bin/python3
for k in range(122, 96, -1):
    print("{:c}".format(k if k % 2 == 0 else k - 32), end="")
