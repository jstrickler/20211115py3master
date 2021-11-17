d1 = dict()   # empty dict
d2 = {'a':43, 'm':11, 'z': 0, 'r': 55}
d3 = {}  # also empty dict


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

print(airports['RDU'])   # DICT[key] LIST[pos]
airports['AUS'] = "Austin"   # keep Austin weird!!
print(airports)
airports['IAH'] = "Houston"
print(airports)
airports['YYZ'] = "Kitchener"
print(airports)

more_airports = {'SEA': 'Seattle', 'MIA': 'Miami', 'JFK': 'New York', 'YYZ': 'Toronto'}

airports.update(more_airports)
print(airports)

print(airports['EWR'])

for code in 'EWR', 'BOS', 'WOMBAT', 'RDU', 'YYZ':
    print(code, airports.get(code), airports.get(code, "No such place"))
print()

print(airports.setdefault('BOS', 'Boston'))
print(airports)

airports['abc'] = "Town 1"   #  ["Town 1", "Town 2", ...]      airports['abc'][0]      dict of lists
airports['abc'] = "Town 2"   # {"town": "blah", "size": blah}  airports['abc']['town']  dict of dicts
airports['abc'] = "Town 3"

print(airports)

data = [1, 2, 3, 4]
airports['spam'] = data
airports['spam'].append(8)
print(airports)

my_image = "this is really an image object..."

airports['image1'] = my_image
print()

del airports['abc']
del airports['spam']
del airports['image1']

#   key   value
for code, city in airports.items():   #  [(k, v), (k, v), ...]
    print(code, city)
print()

for code, city in sorted(airports.items()):
    print(code, city)
print()






























