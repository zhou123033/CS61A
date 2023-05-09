def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25


print(xk(10, 10), xk(10, 6), xk(4, 6), xk(0, 0))

print('----------')
def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print('nothing')


print(how_big(7), how_big(12), how_big(1), how_big(-1))

print('----------')
n = 3
while n >= 0:
    n -= 1
    print(n)

print('----------')
positive = 27
while positive:
    print('positive?')
    positive -= 3

print('----------')
positive = -9
negative = -12
while negative:
    if positive:
        print(negative)
    positive += 3
    negative += 3

print('----------')


def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')


ab(10, 20)
print('----------')


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake


bake(0, 29)
bake(1, "mashed potatoes")