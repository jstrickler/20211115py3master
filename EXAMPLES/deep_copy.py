#!/usr/bin/env python
import copy

data = [
    [1, 2, 3],
    [4, 5, 6],
]

d1 = data # alias for data
d2 = list(data) # shallow copy of data
d3 = copy.deepcopy(data) # deep copy of data
print(id(data), id(d1), id(d2), id(d3))

d1.append("d1")  # same as appending to data
d1[0].append(50) # append to first element of d1

d2.append("d2")   # <6>
d2[0].append(99)  # <7>

d3.append("d3")   # <8>
d3[0].append(500) # <9>

print("data:", data, id(data))
print("d1:", d1, id(d1))
print("d2:", d2, id(d2))
print("d3:", d3, id(d3))
print()

print("id(d1[0]):", id(d1[0]))
print("id(d2[0]):", id(d2[0]))
print("id(d3[0]):", id(d3[0]))

names = ['Fred', 'Mary', 'Bob']

def doit(wallaby):
    wallaby.append("Fritz")
    print("in doit(): wallaby is", wallaby)

doit(names)

doit(['Molly', 'Nellie', 'Seth'])


print(names)





