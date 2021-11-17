
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date"]

print("len(fruits): {}\n".format(len(fruits)))


f1 = sorted(fruits)
print("f1: {}\n".format(f1))

def ignore_case(fruit):
    compare_value = fruit.lower()
    print(f"comparing {fruit} as {compare_value}")
    return compare_value


f2 = sorted(fruits, key=ignore_case)
print()

print("f2: {}\n".format(f2))

# len()
f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def custom_sort(element):
    return len(element), element.lower()

f4 = sorted(fruits, key=custom_sort)
print("f4: {}\n".format(f4))

def wacky(x):
    print("x is", x)
    return x[-1]   # last character

f5 = sorted(fruits, key=wacky)
print("f5: {}\n".format(f5))

# instead of comparing   fruits[x] and fruits[y]
#     it compares        wacky(fruits[x]) and wacky(fruits[y])

#  key function transforms one value from list into version for comparing

f6 = sorted(fruits, key=ignore_case, reverse=True)
print("f6: {}\n".format(f6))


def null(x):
    return x

f7 = sorted(fruits, key=null)
print("f7: {}\n".format(f7))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def custom(p):
    return p[1]

for person in sorted(people, key=custom):
    print(person)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, name in sorted(airports.items()):
    print(code, name)
print('-' * 60)

print(airports.items())

def by_value(item):
    return item[1], item[0]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print('-' * 60)


nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1: {}\n".format(n1))

n2 = sorted(nums, reverse=True)
print("n2: {}\n".format(n2))

n3 = sorted(nums, key=str)
print("n3: {}\n".format(n3))































