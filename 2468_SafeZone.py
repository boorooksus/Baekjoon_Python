from sys import stdin
from collections import deque

n = int(stdin.readline())

h = [[] for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
d = [0 for _ in range(101)]

for i in range(n):
    h[i] = list(map(int, stdin.readline().split()))


def bfs(col, row, height):
    q = deque()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visit[col][row] = True
    q.appendleft((col, row))
    while q:
        cy, cx = q.pop()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny >= 0 and ny < n and nx >= 0 and nx < n\
                and visit[ny][nx] == False and h[ny][nx] > height:
                visit[ny][nx] = True
                q.appendleft((ny, nx))


for i in range(0, 101):
    for j in range(n):
        for k in range(n):
            if visit[j][k] == False and h[j][k] > i:
                bfs(j, k, i)
                d[i] += 1
    if d[i] == 0:
        break
    else:
        visit = [[False for _ in range(n)] for _ in range(n)]

print(max(d))

#문해기 4주차 bfs 유형