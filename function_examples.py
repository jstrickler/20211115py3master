import math

def get_message():
    return "Hello, Python world"

m = get_message()
print(m)

def spam():
    print("Hello from spam()")

result = spam()
print(result)

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

print(circle_area(10))
a = circle_area(75)
print(f"Area of a circle with diameter 75 is {a:.2f}")

def square_area(length, width):
    return length * width

print(square_area(5, 8))
sa = square_area(99, 4203)
print(sa)

def greet(whom="world"):
    print("Hello,", whom)

greet("Bob")
greet("Mom")
greet("world")
greet()

def cgrep(text, *file_names):
    print("file names:", file_names)
    count = 0
    for file_name in file_names:
        with open(file_name) as file_in:
            for line in file_in:
                if text in line:
                    count += 1
    return count

a_count = cgrep('Alice', 'DATA/alice.txt')
print("Alice:", a_count)
print("rabbit:", cgrep('rabbit', 'DATA/alice.txt'))
print("rabbit:", cgrep('rabbit', 'DATA/words.txt', 'DATA/alice.txt'))

# def spam(*a, b):
#     pass


def process_files(file_list):
    pass













