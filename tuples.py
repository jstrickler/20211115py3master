
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

x = (5)

print(person)
print(type(person), len(person))
print(person[0], person[-1])

first_name, last_name, product, dob = person   # iterable unpacking
print(first_name, last_name)

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

print(type(people), type(people[0]), type(people[0][0]), '\n')

for person in people:
    print(person, type(person))
print('-' * 60)

for person in people:
    # first_name, ... = person
    # print(first_name, ...)
    print(person[0], person[1])
print('-' * 60)

for first_name, last_name, product, dob in people:
    #  first_name, last_name, product, dob = people[0]
    #  ...
    print(first_name, last_name)
print('-' * 60)

x = 'a', 5

info = [('a', 5), ('m', 19), ('z', 6), ('e', 42)]
for letter, number in info:
    print(f"{letter} => {number}")







