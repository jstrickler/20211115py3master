import sys
from john.math import geom
# find john/math/geom.py using sys.path

# then create obj named geom for access to module contents
try:
    import spam
except ModuleNotFoundError as err:
    print(err)

print(geom.PI, geom.ANIMAL)

x = geom.circle_area(10)
print(f"{x:.2f}")

print(geom.square_area(55))

print(geom.rectangle_area(8, 22))


# module search algorithm
# 1. current folder
# 2. if environment (shell) variable PYTHONPATH exists
#       search folders in PYTHONPATH from left to right
# 3. Python installation folder

for path in sys.path:
    print(path)
