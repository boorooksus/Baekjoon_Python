from sys import stdin
from queue import PriorityQueue


q = PriorityQueue()
n = int(stdin.readline())
for i in range(n):
    x = int(stdin.readline())

    if x == 0:
        if q.empty():
            print(0)
        else:
            value, sign = q.get()
            print(value * sign)

    else:
        sign = 1
        if x < 0:
            x *= -1
            sign = -1

        q.put((x, sign))


# 런타임 에러