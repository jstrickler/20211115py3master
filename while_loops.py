
i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    user_name = input("What is your name (or q to quit)? ")
    if user_name == 'q':
        break

    if user_name == '':
        continue

    print(f"Hello, {user_name}")


