from carddeck import CardDeck

d1 = CardDeck("Nellie")
d2 = CardDeck("Andy")
d3 = CardDeck("Little Bear")

print(d1, type(d1))

# print(str(d1))  # d1.__str__()

# <warning>CHEATING</warning>
print(d1.dealer_name)  # not d1.dealer()
d1.dealer_name = "Bob"
print(d1.dealer_name)
try:
    d1.dealer_name = 5.9
except TypeError as err:
    print(err)
print(d1.dealer_name)

print(dir(d1))
print()


