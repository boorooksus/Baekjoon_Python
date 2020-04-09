from sys import stdin
import queue

n, m = map(int, stdin.readline().split())
check = [[False for i in range(m)] for j in range(n)]
arr = []
for i in range(n):
    row_str = stdin.readline()
    arr.append(row_str)
cnt = 1

def bfs(col, row):
    global n, m
    global cnt
    q = queue.Queue()
    q.put([col, row, cnt])

    while(1):
        #way = 0
        step = q.qsize()
        #cnt -= step
        x_list = q.get()
        x_col = x_list[0]
        x_row = x_list[1]
        x_cnt = x_list[2]
        '''if q.empty():
            cnt += 1'''
        #check[x_col][x_row] = True

        if x_col == n - 1 and x_row == m - 1:
            #cnt += 1
            print(x_cnt)
            break
        if x_col != 0 and check[x_col - 1][x_row] == False\
                and arr[x_col - 1][x_row] == '1':
            q.put([x_col - 1, x_row, x_cnt + 1])
            check[x_col - 1][x_row] = True
            #way += 1
        if x_col < n - 1 and check[x_col + 1][x_row] == False\
                and arr[x_col + 1][x_row] == '1':
            q.put([x_col + 1, x_row, x_cnt + 1])
            check[x_col + 1][x_row] = True
            #way += 1
        if x_row != 0 and check[x_col][x_row - 1] == False\
                and arr[x_col][x_row - 1] == '1':
            q.put([x_col, x_row - 1, x_cnt + 1])
            check[x_col][x_row - 1] = True
            #way += 1
        if x_row < m - 1 and check[x_col][x_row + 1] == False\
                and arr[x_col][x_row + 1] == '1':
            q.put([x_col, x_row + 1, x_cnt + 1])
            check[x_col][x_row + 1] = True
            #way += 1
        #cnt = cnt - way + 1
    return

bfs(0, 0)

