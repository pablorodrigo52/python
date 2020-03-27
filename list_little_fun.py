#Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
import random

a = random.sample(xrange(100), 10)
b = random.sample(xrange(100), 20)
c = []

print("List1",a)
print("List2",b)
for x in a:
    if ((x in b) & (x not in c)):
        c.append(x)
print(c)
