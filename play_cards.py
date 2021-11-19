from carddeck import CardDeck
from jokerdeck import JokerDeck

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

#  str(x)  ->  x.__str__()

d1.shuffle()

c = d1.draw()
print(c, repr(c))
print(c.suit, c.rank)

print(d1.cards)

d2 = CardDeck("Oscar")
print(d1)
print(d2)

j1 = JokerDeck("Bonnie")
print(j1)
j1.shuffle()
print(j1.cards)
