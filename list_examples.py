list1 = list()   # list list1 = new list();
list2 = ['red', 'purple', 'beige']
list3 = []


print(list1, list2, list3)
print(len(list1), len(list2))

a = "abc"
b = b"abc"
print(list(a), list(b))

cities = ['Austin', 'Waco', 'Durham', 'New York', 'Charlotte']
print(cities)
print(cities[0], cities[3])
print(len(cities))
print(cities)
cities.insert(0, 'Poughkeepsie')
cities.insert(3, "Taos")
print(cities)
cities[1] = "Plano"
print(cities)
cities.insert(len(cities)+1, "Miami")  # don't do this
print(cities)
cities.append("Chicago")  # do this
print(cities)

more_cities = ["Pittsburgh", "Topeka", "Eugene"]
cities.extend(more_cities)
print(cities)

#  LIST.insert(pos, obj)  LIST.append(obj)   LIST.extend(iterable)
#  LIST[pos] = VALUE

del cities[1]   # del OBJ    del OBJ[index]
print(cities)

c = cities.pop()
print(c)
print(cities)

c = cities.pop(4)
print(c)
print(cities)

cities.remove('Miami')
print(cities)

print('Chicago' in cities)
print("Raleigh" in cities)

print(cities.count('Chicago'))
print(cities.count('Raleigh'))
cities.append('Chicago')
cities.insert(3, 'Chicago')

print(cities.index('Chicago', 4))

# del LIST[pos]    LIST.pop(pos=-1)    LIST.remove(value)


print(cities)

print(cities[0], cities[5], cities[-1], cities[-2])
print(cities[len(cities) - 1])

print(cities[0:5])
print(cities[3:8])
print(cities[7:9])
print(cities[:5])   # first 5
print(cities[8:])   # index 8 to end
print(cities[-5:])  # last 5

#  LIST[start:stop]   LIST[start:stop:step]

s = "Happy Birthday"
print(s[:5])
print(s[2:4])
print(s[-3:])
print(list(s))

a = "hello"
print(list(a))

print(cities)
print("-" * 60)

for city in cities:  # cf. "foreach"
    # city = cities[0]
    # city = cities[1]
    # ...
    # city = cities[-1]
    print(city)

print("-" * 60)
print(city)

s = "abc"
for letter in s:
    print(letter)
print()

# foreach
for city in 'Durham', 'Waco', 'Albany', 'Springfield', 'Topeka':
    pass

print(city)

#  for (i = 0; i < 3; i++) {
#  }

print(cities)
print(len(cities), min(cities), max(cities))
print(sorted(cities))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(sum(nums))

rc = reversed(cities)
print(rc)  # generator
for city in rc:
    print(city, end=' ')
print('\n')

for city in rc:
    print(city, end=' ')
print('\n')

rc2 = list(reversed(cities))
print(rc2)


rr = reversed(cities)
a = list(rr)
b = list(rr)
print("a:", a, '\n')
print("b:", b, '\n')


capitals = ['Raleigh', 'Austin', 'Albany']
states = ['NC', 'TX', 'NY', 'CA']

state_capitals = zip(capitals, states)

print(state_capitals)

for x in state_capitals:
    print(x)
print('-' * 60)

for city, state in zip(capitals, states):
    print(city, state)
print('-' * 60)

m = 1, 2, 3, 4, 5, 6
print(list(zip(capitals, states, m)))
print()


i = 0
for city in cities:
    print(i, city)
    i += 1
print()

for i, city in enumerate(cities):
    print(i, city)
print()

print(list(enumerate(cities)))

a = [1, 2, 3]
b = [8, 9, 10]
print(a + b)

print('-' * 10)
print("wombat" * 5)
flags = [True] * 10
print(flags)












































