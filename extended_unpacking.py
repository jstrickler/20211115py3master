

car = 2003, 'Chevrolet', 'Suburban'

year, make, model = car

print(year, model, make)

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

w, *x, y, z = values
print(w, x, y, z)


s = "abcdef"

x, y, *z = s
print(x, y, z)








