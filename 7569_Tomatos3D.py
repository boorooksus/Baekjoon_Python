from sys import stdin
from collections import deque

#m: 가로 칸 수, n: 세로 칸 수, h:높이
m, n, h = map(int, stdin.readline().split())
#토마토 정보를 3차원 리스트로 입력
container = []
for i in range(h):
    layer = []
    for j in range(n):
        layer.append(list(map(int, stdin.readline().split())))
    container.append(layer)

q = deque()
day = 0
maxsize = [h, n, m]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if container[i][j][k] == 1:
                q.appendleft([i, j, k, day])

def bfs(h, n, m):
    global day
    while(1):
        #토마토가 다 익었는지 확인
        isDone = True
        for i in range(h):
            for j in range(n):
                if 0 in container[i][j]:
                    isDone = False
                    break
        if isDone == True:
            if day == 0:
                print(0)
            else:
                print(day + 1)
            return

        # q가 비게되면 토마토가 모두 익지 못하는 상황
        if len(q) == 0:
            print(-1)
            return
        #bfs
        tomato = q.pop()
        day = tomato[3]
        nz = [-1, 0, 0]
        ny = [0, -1, 0]
        nx = [0, 0, -1]
        mz = [1, 0, 0]
        my = [0, 1, 0]
        mx = [0, 0, 1]
        for i in range(3):
            if tomato[i] > 0 and\
                    container[tomato[0] + nz[i]][tomato[1] + ny[i]][tomato[2] + nx[i]] == 0:
                '''a = tomato[0] + z[i]
                b = tomato[1] + y[i]
                c = tomato[2] + x[i]'''
                #print(a, b, c)
                q.appendleft([tomato[0] + nz[i], tomato[1] + ny[i], tomato[2] + nx[i], day + 1])
                container[tomato[0] + nz[i]][tomato[1] + ny[i]][tomato[2] + nx[i]] = 1
            if tomato[i] < maxsize[i] - 1 and\
                    container[tomato[0] + mz[i]][tomato[1] + my[i]][tomato[2] + mx[i]] == 0:
                q.appendleft([tomato[0] + mz[i], tomato[1] + my[i], tomato[2] + mx[i], day + 1])
                container[tomato[0] + mz[i]][tomato[1] + my[i]][tomato[2] + mx[i]] = 1


bfs(h, n, m)




