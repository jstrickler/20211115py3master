import re

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

#   [EXPR for VAR in ITERABLE]
#   ITERABLE => list tuple dict set generator str bytes
#   [EXPR for VAR in ITERABLE if CONDITION]
f2 = [f.upper() for f in fruits if f.startswith(('p', 'a'))]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

f4 = [f for f in fruits if len(f) > 8]
print("f4: {}\n".format(f4))



cities = ['Chicago', 'Topeka', 'Pittsburgh', 'Chicago', 'Charlotte', 'Durham', 'Topeka', 'Chicago', 'Taos', 'Waco', 'Durham', 'Poughkeepsie']

c2 = [c for c in cities if c != 'Chicago']
print("c2: {}\n".format(c2))

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

last_names = [p[1] for p in people]
print("last_names: {}\n".format(last_names))

full_names = [f"{p[0]} {p[1]}" for p in people]
print("full_names: {}\n".format(full_names))

fn_gen = (f"{p[0]} {p[1]}" for p in people)
print(fn_gen)
for full_name in fn_gen:
    print(full_name)
print()

print(type(full_names), type(fn_gen))

from types import GeneratorType

if isinstance(full_names, list):
    print("LIST")

if isinstance(fn_gen, GeneratorType):
    print("GEN")

import inspect

print(inspect.isgenerator(fn_gen))
print(inspect.isgenerator(full_names))









