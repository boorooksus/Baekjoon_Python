from sys import stdin
import heapq

n = int(stdin.readline())
h = []

for i in range(n):
    x = int(stdin.readline())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, x)
