from random import randrange
p = 809
q = 101
h = 2
g = pow(h, (p - 1) // q, p)
x = randrange(1, q)
y = pow(g, x, p)

def enc(m):
    k = randrange(2, q)
    c1 = pow(g, k, p)
    c2 = m * pow(y, k, p)
    return (c1, c2)

def dec(ct):
    c1, c2 = ct
    return c2 // pow(c1, x, p)

count = 10000
testset = []
while count > 0:
    m = randrange(3, 2 ** 64)
    ct = enc(m)
    testset.append(pow(ct[0], x, p))
    dc = dec(ct)
    assert dc == m
    count -= 1

print("unique ciphertexts: {}".format(len(set(testset))))
