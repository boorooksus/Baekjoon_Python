from sys import stdin
from collections import deque

maze = [['' for _ in range(50)] for _ in range(50)]
visit = [[[0 for _ in range(64)] for _ in range(50)] for _ in range(50)]

n, m = map(int, stdin.readline().split())
sx = 0
sy = 0
ex = 0
ey = 0
mask = 0
for i in range(n):
    line = stdin.readline().strip()
    for j in range(m):
        maze[i][j] = line[j]
        if line[j] == '0':
            sy = i
            sx = j
        elif line[j] == '1':
            ey = i
            ex = j
        elif ord(line[j]) > 96:
            #mask += 10 ** (ord(line[j]) - 97)
            mask += int(format(2 ** (ord(line[j]) - 97)))

def bfs(sy, sx, ey, ex, n, m, mask):
    ans = 0
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    dq = deque()
    dq.appendleft((sy, sx, mask))
    visit[sy][sx][mask] = 1
    while dq:
        ans += 1
        ql = len(dq)
        for _ in range(ql):
            cy, cx, cm = dq.pop()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if cx == 0 and cy == 0:
                    here = 0
                if ny >= 0 and ny < n and nx >= 0 and nx < m\
                        and visit[ny][nx][cm] == 0:
                    roomChar = maze[ny][nx]
                    if roomChar == '1':
                        print(ans)
                        return
                    elif roomChar == '#':
                        continue
                    elif ord(roomChar) > 96:
                        idx = ord(roomChar) - 97
                        if cm >= 2 ** idx and bin(cm)[-idx - 1] == '1':
                            nm = cm - 2 ** idx
                            visit[ny][nx][nm] = 1
                            dq.appendleft((ny, nx, nm))
                        else:
                            visit[ny][nx][cm] = 1
                            dq.appendleft((ny, nx, cm))
                    elif ord(roomChar) > 64 and ord(roomChar) < 71:
                        idx = ord(roomChar) - 65
                        if cm < 2 ** idx or bin(cm)[-idx - 1] == '0':
                            visit[ny][nx][cm] = 1
                            dq.appendleft((ny, nx, cm))
                        else:
                            continue
                    else:
                        visit[ny][nx][cm] = 1
                        dq.appendleft((ny, nx, cm))
    print(-1)
    return


bfs(sy, sx, ey, ex, n, m, mask)






