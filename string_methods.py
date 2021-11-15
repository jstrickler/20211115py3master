a = "spam"
b = "ham"
c = a + b
print(c, '\n')

actor = "Chris Hemsworth"
print(type(actor), len(actor))

print(actor.upper())

print("abc".upper())

aa = actor.upper()
print(aa, actor, actor.lower())
print(actor)

print(actor.count('h'))
print(actor.count('H'))

print(actor.lower().count('h'))

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print("worth" in actor)  # substr in str
print("value" in actor)

print(actor.find('Chris'), actor.find('Liam'))
print(actor.find('Hem'), actor.lower().find('hem'))
print()

s = "     All my exes live in Texas      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s2 = "xxxxxxxxxxxxyxxxxxxxxAll my exes live in Texasxyxyyyyyyyxxxxxxxyxyxyxyxyyyyyyx"
print("|" + s2.lstrip("xy") + "|")
print("|" + s2.rstrip("xy") + "|")
print("|" + s2.strip("xy") + "|")
print()


s3 = "double double toil and trouble"
words = s3.split()
print("words:", words)
w2 = "//".join(words)
print("w2:", w2)












