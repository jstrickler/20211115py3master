bob_countries = ['Spain', 'Portugal', 'Burkina Faso', 'Bulgaria', 'Spain', 'Spain', 'Japan', 'New Zealand', 'Mali']

delilah_countries = ['Mali', 'Burkina Faso', 'Egypt', 'Spain', 'France', 'Portugal', 'Estonia']

bob = set(bob_countries)
delilah = set(delilah_countries)

print(bob)
print(delilah)

print("Common:", bob & delilah)  # intersection
print("NOT Common:", bob ^ delilah)  # xor
print("ALL:", bob | delilah)  # union
print("Bob only:", bob - delilah)
print("Delilah only:", delilah - bob)

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
print(set(food))

