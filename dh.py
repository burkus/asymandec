from random import randrange

p = 67
g1 = 20 # primitive root
g2 = 21 # not primitive root

g1s = []
g2s = []

tests = 1000
width = 1000
for i in range(tests):
    a = randrange(1, p)
    b = randrange(1, p)
    A = pow(g1, a, p)
    B = pow(g1, b, p)
    secret = pow(A, b, p)
    g1s.append(secret)

for i in range(tests):
    a = randrange(1, p)
    b = randrange(1, p)
    A = pow(g2, a, p)
    B = pow(g2, b, p)
    secret = pow(A, b, p)
    g2s.append(secret)

print("primitive root set size is {}".format(len(set(g1s))))
print("non primitive root set size is {}".format(len(set(g2s))))
