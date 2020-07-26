from sys import stdin
import heapq


h = []
n = int(stdin.readline())
for i in range(n):
    x = int(stdin.readline())

    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            value, sign = heapq.heappop(h)
            print(value * sign)

    else:
        sign = 1
        if x < 0:
            x *= -1
            sign = -1

        heapq.heappush(h, (x, sign))


# 우선순위 큐
# heapq