import os

person = "Fred Flintstone"
city = "Bedrock"
value = 23.39760293

print(person, city, value)  #  print(str(person), str(city), str(value))
print("OK")

print(person, end=" ")
print("WOMBAT", end = "! ")
print(city)

a = "go\n"
b = "stop"

print(a, end="")
print(b)

print(person, city, value, sep="::")

print(person, "lives in", city)

fmt = "{} lives in {}"

s = fmt.format(person, city)
print(s)
print("{} lives in {}".format(person, city))
print(f"{person} lives in {city}")   # f-string  f""  f'' f""""""  f''''''


print("The value is {:.2f}".format(value))
print(f"The value is {value:.2f}")

print("%s lives in %s" % (person, city))
print("The value is %.2f" % (value))















