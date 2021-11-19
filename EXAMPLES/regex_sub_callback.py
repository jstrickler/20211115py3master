#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo Z883  consequat. Duis aute irure dolor in reprehenderit in  
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

#  my $rx_code = qr/(?P<letter>[A-Z])(?P<number>\d{2,3})/i;
#  if ($foo ~= /$rx_code/) { }

rx_code = re.compile(r'(?P<letter>[A-Z])(?P<number>\d{2,3})', re.I)


def update_code(m):  # <1>
#    letter = m.group('letter').upper()
    letter = m.group(1).upper()
    number = int(m.group('number'))
    return '{}{:04d}'.format(letter, number)  # <2>


s2 = rx_code.sub(update_code, s)  # <3>
print(s2, '\n')

pattern = "(?P<hour>\d{2}):(?P<minute>\d{2})\s*(?P<ampm>[AP])M"

text = [
    "It is 12:32  AM in Austin",
    "Please turn out the lights at 10:00 PM",
    "We call 04:00AM oh dark thirty",
]

for t in text:
    print("Text:", t)
    m = re.search(pattern, t)
    if m:
        print("group 0:", m.group(0))
        print("group 1:", m.group('hour'))
        print("group 2:", m.group('minute'))
        print("group 3:", m.group('ampm'))
        print("=" * 20)


p = r"\d{3}-\d{2}-(\d{4})"


#   p1  p2 p3  p4

pattern = r"(?:p1)|(?:p2)|(?:p3)|(?:p4)"







