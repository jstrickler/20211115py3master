from types import GeneratorType

test_data = ['one', 'two', 'three']

class g_class:
    def __init__(self, max_value):
        self.count = 0
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.max_value:
            raise StopIteration
        count = self.count
        self.count += 1
        return count

def g_func():
   yield True

def is_generator(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__next__') and not callable(obj)


iterables = {
    "enumerate()": enumerate(test_data),
    "reversed()": reversed(test_data),
    "zip()": zip([1,2,3], test_data),
    "open()": open("/dev/null"),
    "generator expression": (d.upper() for d in test_data),
    "generator function result": g_func(),
    "generator class instance": g_class(5),
    "range()": range(5),
    "range": range,
    "dict.items()": {'a': 0}.items(),
    "generator function": g_func,
    "generator class": g_class,
    "list": list(),
    "tuple": tuple(),
    "dict": dict(),
    "set": set(),
    "string": "abc",
    "bytes": b"abc",
    "int": 5,
    "None": None,
}

fmt = "{:28s} {!s:15} {!s:10} {!s:10} {!s:10} {!s:10} {!s:15}"
header_names = "Object", "GeneratorType", "__iter__", "__next__", "__len__", "callable", 'is_generator'
header = fmt.format(*header_names)
print(header)
print('-' * len(header))
for name, iterable in iterables.items():
    print(
        fmt.format(
            name,
            isinstance(iterable, GeneratorType),
            hasattr(iterable, "__iter__"),
            hasattr(iterable, "__next__"),
            hasattr(iterable, "__len__"),
            callable(iterable),
            is_generator(iterable),
        )
    )
