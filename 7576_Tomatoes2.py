from sys import stdin
from collections import deque

#m : 가로 , n : 세로
m, n =  map(int, stdin.readline().split())
box = []
for i in range(n):
    box.append(list(map(int, stdin.readline().split())))

def bfs(n, m):
    isDone = True
    for i in range(n):
        if 0 in box[i]:
            isDone = False
    if isDone == True:
        print(0)
        return

    q = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.appendleft((i, j))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ans = -1
    while q:
        qlen = len(q)
        ans += 1
        for _ in range(qlen):
            col, row = q.pop()
            for i in range(4):
                nxty = col + dy[i]
                nxtx = row + dx[i]
                if nxty >= 0 and nxty < n and nxtx >= 0 and nxtx < m\
                    and box[nxty][nxtx] == 0:
                    box[nxty][nxtx] = 1
                    q.appendleft((nxty, nxtx))
    isDone = True
    for i in range(n):
        if 0 in box[i]:
            isDone = False
    if isDone == False:
        print(-1)
        return
    print(ans)

bfs(n, m)