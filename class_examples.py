
colors = list()    # create instance of list class
colors.append('blue')
colors.insert(0, 'red')

x = int(5)      #  x = 5

print(colors, x)

names = ['Fred', 'Mary', 'Lisa', 'Steve']

with open('DATA/mary.txt') as mary_in:
    print(mary_in.readline())

print(type(mary_in))

class Dog:   # definition (~blueprint)
    def bark(self):
        print("Woof! woof!")


d1 = Dog()  # Pitbull    instance of Dog()
d2 = Dog()  # golden retriever
d3 = Dog()  # English shepherd

for dog in d1, d2, d3:
    dog.bark()


















