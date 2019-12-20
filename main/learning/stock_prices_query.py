from random import randint


def s():
    a = {}
    for i in range(50):
        res = randint(1, 365)
        if res in a:
            return True
        a[res] = True
    return False


total = 0
for i in range(10000):
    if s():
        total += 1
print(total / 10000)
