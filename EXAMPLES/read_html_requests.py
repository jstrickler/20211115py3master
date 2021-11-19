#!/usr/bin/env python
import requests

response = requests.get("https://www.python.org")  # <1>
#   .get() .put() .post() .paste() .head() .delete()


print(response.status_code)

for header, value in sorted(response.headers.items()): # <2>
    print(header, value)
print()

print(response.text[:200])   # <3>
print('...')
print(response.text[-200:])   # <4>
