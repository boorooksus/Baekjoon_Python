from sys import stdin
from collections import deque
import queue

m, n = map(int, stdin.readline().split())
arr = []
#2차원 배열로 저장
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

tomato_day = 0
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.appendleft([i, j, tomato_day])

def bfs():
    global tomato_day
    while(1):
        if len(q) == 0:
            isDone = True
            '''for i in range(n):
                if 0 in arr[i]:
                    isDone = False'''
            if 0 in arr:
                isDone = False
            # 모두 익었을 때
            if isDone == True:
                print(tomato_day)
                return
            #안익은 토마토가 있을 때
            else:
                print(-1)
                return

        tomato_list = q.pop()
        tomato_col = tomato_list[0]
        tomato_row = tomato_list[1]
        tomato_day = tomato_list[2]

        if tomato_col > 0 and arr[tomato_col - 1][tomato_row] == 0:
            q.appendleft([tomato_col - 1, tomato_row, tomato_day + 1])
            arr[tomato_col - 1][tomato_row] = 1
        if tomato_col < n - 1 and arr[tomato_col + 1][tomato_row] == 0:
            q.appendleft([tomato_col + 1, tomato_row, tomato_day + 1])
            arr[tomato_col + 1][tomato_row] = 1
        if tomato_row > 0 and arr[tomato_col][tomato_row - 1] == 0:
            q.appendleft([tomato_col, tomato_row - 1, tomato_day + 1])
            arr[tomato_col][tomato_row - 1] = 1
        if tomato_row < m - 1 and arr[tomato_col][tomato_row + 1] == 0:
            q.appendleft([tomato_col, tomato_row + 1, tomato_day + 1])
            arr[tomato_col][tomato_row + 1] = 1

bfs()




