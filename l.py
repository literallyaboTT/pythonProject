import random
d = {'a':1, 'b':2, 'c':3, 'd':4}
l = list(d.keys())
random.shuffle(l)
d = dict(l)

print(d)


