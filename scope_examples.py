
x = 100  # GLOBAL


def spam():
    y = 42  # LOCAL
    print("in spam(): x is", x)
    print("in spam(): y is", y)

spam()

print("In main: x is", x)
# print("In main: y is", y)  y was LOCAL to spam()


