from sys import stdin
from collections import deque

def bfs(sx, sy, ex, ey, l):
    if sx == ex and sy == ey:
        return 0
    board = [[0 for _ in range(l)] for _ in range(l)]
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    ans = 0
    q = deque()
    board[sy][sx] = 1
    q.appendleft((sy, sx))
    while q:
        ans += 1
        ql = len(q)
        for _ in range(ql):
            cury, curx = q.pop()
            for i in range(8):
                nxty = cury + dy[i]
                nxtx = curx + dx[i]
                if nxty >= 0 and nxty < l and nxtx >= 0 and nxtx < l\
                    and board[nxty][nxtx] == 0:
                    if nxty == ey and nxtx == ex:
                        return ans
                    board[nxty][nxtx] = 1
                    q.appendleft((nxty, nxtx))
    return 0

n = int(stdin.readline())
for _ in range(n):
    l = int(stdin.readline()) #size of chess board
    sx, sy = map(int, stdin.readline().split()) #start point
    ex, ey = map(int, stdin.readline().split()) #end point
    print(bfs(sx, sy, ex, ey, l))