

def spam():
    print("Hello from spam()")

def call_a_function(func):
    print(func)
    func()  # invoke the passed-in function

call_a_function(spam)

def ham():
    print("Hello from ham()")

call_a_function(ham)


def foo():
    return 100

print(type(foo), type(foo()))




