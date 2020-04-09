from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

t = int(stdin.readline()) # test cases

def dfs(col, row):
    if check[col][row] == True or arr[col][row] == 0:
        return
    check[col][row] = True
    if col != 0:
        dfs(col - 1, row)
    if col != len(arr) - 1:
        dfs(col + 1, row)
    if row != 0:
        dfs(col, row - 1)
    if row != len(arr[col]) - 1:
        dfs(col, row + 1)



for test_cases in range(t):
    #m : row, n : col, k : number of cabbage
    m, n, k = map(int, stdin.readline().split())
    # number of worm
    cnt = 0
    arr = [[0 for i in range(m)]for j in range(n)]
    check = [[False for i in range(m)] for j in range(n)]
    for i in range(k):
        x, y = map(int, stdin.readline().split())
        arr[y][x] = 1
    for col in range(n):
        for row in range(m):
            if arr[col][row] == 1 and check[col][row] == False:
                cnt += 1
                dfs(col, row)
    print(cnt)
