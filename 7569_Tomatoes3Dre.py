from sys import stdin
from collections import deque

def bfs(m, n, h):
    '''finished = True
    for i in range(h):
        for j in range(n):
            if 0 in boxes[i][j]:
                finished = False
    if finished:
        return 0'''
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if boxes[i][j][k] == 1:
                    q.appendleft((i, j, k))

    ans = -1
    while q:
        ans += 1
        ql = len(q)
        for _ in range(ql):
            layer, col, row = q.pop()
            for i in range(6):
                nz = layer + dz[i]
                ny = col + dy[i]
                nx = row + dx[i]
                if nz >= 0 and nz < h and ny >= 0 and ny < n\
                    and nx >= 0 and nx < m and\
                    boxes[nz][ny][nx] == 0:
                    boxes[nz][ny][nx] = 1
                    q.appendleft((nz, ny, nx))


    for i in range(h):
        for j in range(n):
            if 0 in boxes[i][j]:
                return -1
    return ans


#m, n : size of box, h : layers of boxes
m, n, h = map(int, stdin.readline().split())
boxes = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        boxes[i].append(list(map(int, stdin.readline().split())))
#[[[00000][00000][00000]],[[00000][00100][00000]]
print(bfs(m, n, h))
