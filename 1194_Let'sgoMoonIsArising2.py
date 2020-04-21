from sys import stdin
from collections import deque

maze = [['' for _ in range(50)] for _ in range(50)]
visit = [[[0 for _ in range(64)] for _ in range(50)] for _ in range(50)]

n, m = map(int, stdin.readline().split())
sx = 0
sy = 0
mask = 0
for i in range(n):
    line = stdin.readline().strip()
    for j in range(m):
        maze[i][j] = line[j]
        if line[j] == '0':
            sy = i
            sx = j
        elif ord(line[j]) > 96:
            #mask += 10 ** (ord(line[j]) - 97)
            mask += int(format(2 ** (ord(line[j]) - 97)))

def bfs(sy, sx, n, m, mask):
    ans = 0
    keyGot = 0
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    dq = deque()
    dq.appendleft((sy, sx, 0))
    visit[sy][sx][0] = 1
    while dq:
        ans += 1
        ql = len(dq)
        for _ in range(ql):
            cy, cx, ck = dq.pop()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if ny >= 0 and ny < n and nx >= 0 and nx < m\
                        and visit[ny][nx][ck] == 0:
                    roomChar = maze[ny][nx]
                    if roomChar == '1':
                        print(ans)
                        return
                    elif roomChar == '#':
                        continue
                    elif ord(roomChar) > 96:
                        idx = ord(roomChar) - 97
                        if ck < 2 ** idx or bin(ck)[-idx - 1] == '0':
                            nk = ck + 2 ** idx
                            visit[ny][nx][nk] = 1
                            dq.appendleft((ny, nx, nk))
                        else:
                            visit[ny][nx][ck] = 1
                            dq.appendleft((ny, nx, ck))
                    elif ord(roomChar) > 64 and ord(roomChar) < 71:
                        idx = ord(roomChar) - 65
                        if ck >= 2 ** idx and bin(ck)[-idx - 1] == '1':
                            visit[ny][nx][ck] = 1
                            dq.appendleft((ny, nx, ck))
                        else:
                            continue
                    else:
                        visit[ny][nx][ck] = 1
                        dq.appendleft((ny, nx, ck))
    print(-1)
    return


bfs(sy, sx, n, m, mask)

#문해기 5주차 2번 유형
#좌물쇠는 있는데 열쇠는 없는 경우 있을 수 있음
#참고 : https://jaimemin.tistory.com/773