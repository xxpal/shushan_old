import math

for i in range(10000):
    x1 = i + 100
    x2 = (math.floor(math.sqrt(x1)))**2
    x3 = (int(math.sqrt(x1)))**2

    y1 = i + 268
    y2 = (math.floor(math.sqrt(y1)))**2
    y3 = int(math.sqrt(y1))**2

    flag = ((x1 == x3) and (y1 == y3))
    print('i = {}, flag = {}'.format(i, flag))

    if flag:
        print('The perfect square within 10000 is {}.'.format(i))
        break
