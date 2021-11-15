#!/usr/bin/env python
from getpass import getpass

name = input("What is your name: ")
quest = input("What is your quest? ")
print(name, "seeks", quest)

raw_num = input("Enter number: ")  # <1>
num = float(raw_num)  # <2>

print("2 times", num, "is ", 2 * num)

password = getpass("What is your secret password? ")


