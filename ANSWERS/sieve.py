#!/usr/bin/env python

import sys

limit = 1000000
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

flags = [True] * limit

print("2", end=" ")
for num in range(3, limit, 2):
    # print("start of loop:", flags)
    if flags[num]:
        print(num, end=' ')
        for multiple_of_num in range(2 * num, limit, num):
            flags[multiple_of_num] = False
