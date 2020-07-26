from sys import stdin
from collections import deque


ans = 0
n, p = map(int, stdin.readline().split())
visit = [[0 for _ in range(n+1)] for _ in range(n + 1)]
edge = [[] for _ in range(n + 1)]
for _ in range(p):
    a, b = map(int, stdin.readline().split())
    edge[a].append(b)
    #edge[b].append(a)

while True:
    d = [-1 for _ in range(n + 1)]
    q = deque()
    q.appendleft(1)
    while q:
        x = q.pop()
        for y in edge[x]:
            if visit[x][y] < 1 and d[y] == -1:
                q.appendleft(y)
                d[y] = x
                if y == 2:
                    break

    if d[2] == -1:
        break

    cur = 2
    while cur != 1:
        visit[d[cur]][cur] += 1
        visit[cur][d[cur]] -= 1
        cur = d[cur]
    ans += 1

print(ans)