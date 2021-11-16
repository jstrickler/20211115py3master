import csv

file_path = "DATA/mary.txt"

file_obj = open(file_path, 'r')
#  read file here...
file_obj.close()


with open(file_path) as mary_in:   # mary_in.__exit__(...)
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove  \n \r ' ' \t \f
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()   # read entire file into one string
    print("normal:")
    print(contents)
    print("raw:")
    print(repr(contents))
print('-' * 60)

with open(file_path) as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/parrot.txt') as parrot_in:
    for raw_line in parrot_in:
        if "guy" in raw_line:
            print(raw_line.rstrip())
print('-' * 60)

with open('DATA/words.txt') as words_in:
    count = 0
    for line in words_in:
        if line.rstrip().endswith('x'):
            count += 1
print(f"{count} lines end with x")

state = "Massachusetts"
with open('DATA/presidents.txt') as pres_in:
    with open('presidents.csv', 'w') as pres_out:
        with open('presidents.tsv', 'w') as pres_tab_out:
            wtr = csv.writer(pres_out, lineterminator="\n")
            count = 0
            presidents = []
            for raw_line in pres_in:
                line = raw_line.rstrip()
                fields = line.split(':')
                term, last_name, first_name, dob, dod, bplace, bstate, took_office, left_office, party = fields
                if bstate == state:
                    count += 1
                    record = first_name, last_name
                    presidents.append(record)
                    wtr.writerow(fields)
                    pres_tab_out.write('\t'.join(fields) + '\n')

print(f"{count} presidents are from {state}")
print("presidents list:", presidents)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

with open('fruits.txt') as fruits_in:
    with open('ufruits.txt', 'w') as fruits_out:
        for line in fruits_in:
            fruits_out.write(line.upper())

#  file_path = "//foo/bar/blah/fruit.txt"    #  \\myserver\myfolder\other_folder\file.txt
#  file_path = "C:/foo/bar/blah.fruit.txt"









