#!/usr/bin/env python

fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']  # list
name = "Eric Idle"   # str
knight = 'King', 'Arthur', 'Britain'   # tuple
data = b'abc\xFF'  # bytes (sorta binary str)

print(fruits[3])  # <1>
print(name[0])  # <2>
print(knight[1])  # <3>
print(data[0], data[3])

print(len(fruits), len(name), len(knight), len(data))

more_data = bytes([5, 19, 221, 8, 66, 102, 48])
print(more_data)
