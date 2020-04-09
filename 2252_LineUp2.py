from sys import stdin
from _collections import deque

n, m = map(int, stdin.readline().split())
order = [[0] for i in range(n + 1)]
inDegree = [0 for j in range(n + 1)]
q = deque()

for i in range(m):
    a, b = map(int, stdin.readline().split())
    order[a].append(b)
    inDegree[b] += 1

for j in range(1, n + 1):
    if inDegree[j] == 0:
        q.appendleft(j)

for i in range(1, n + 1):
    x = q.pop()
    print(x, end=' ')
    if len(order[x]) == 1:
        continue
    for j in order[x][1:]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            q.appendleft(j)


