from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print('-' * 60)

for name, data in knight_data.items():
    print(name, data)
print('-' * 60)

for name, data in knight_data.items():
    print(data[0], name)
print('-' * 60)

names_to_remove = ['Galahad', 'Lancelot']

kd2 = {name.upper():data for name, data in knight_data.items() if name not in names_to_remove}
pprint(kd2)
print('-' * 60)

for name in names_to_remove:
    del knight_data[name]

pprint(knight_data)
print('-' * 60)




