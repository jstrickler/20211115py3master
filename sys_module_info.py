import sys

print(sys.version)

print(sys.version_info)

if sys.version_info.minor < 6:
    print("Sorry, Python 3.6 or later required")
    sys.exit(1)

print(sys.version_info[1])

print(sys.prefix)
print(sys.executable)
print()
print("sys.path:")
for path in sys.path:
    print(path)
print()

if sys.platform == 'win32':
    print("I'm on Windows")
elif sys.platform == 'darwin':
    print("I'm on Mac")
elif sys.platform.startswith('linux'):
    print("I'm on Linux")
else:
    print("I'm probably on some Unix variant")


import re
import carddeck

print(sys.modules['re'])
print(sys.modules['carddeck'])

xx = sys.modules['re']

text = "this is only a test"
print(xx.findall(r'\bo[a-z]+', text))

#  sys.stdin  sys.stdout  sys.stderr

sys.stdout.write("Hello weird world\n")

print("We have a problem here", file=sys.stderr)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('myfruits.txt', 'a') as fruits_out:
    for fruit in fruits:
        print(fruit.upper(), file=fruits_out)







