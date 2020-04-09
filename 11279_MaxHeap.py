from sys import stdin
from queue import PriorityQueue
MAX = 100000
q = PriorityQueue()

n = int(stdin.readline())
for i in range(n):
    x = int(stdin.readline())
    if x == 0:
        if q.empty():
            print(0)
        else:
            print(MAX - q.get())
    else:
        q.put(MAX - x)


#우선순위큐, 최대 힙
#heapq도 사용 가능
