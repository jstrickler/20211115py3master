import os
from subprocess import run, PIPE

print("Hello, Python world!")
print(os.getenv('USERNAME'))

os.system('hostname')

result = run('hostname', stdout=PIPE)

print(result.stdout.decode())


