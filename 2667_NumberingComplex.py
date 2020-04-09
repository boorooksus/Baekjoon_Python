from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

n = int(stdin.readline()) #size of map
arr = []
for i in range(n):
    row_str = stdin.readline()
    arr.append(row_str)
houseCnt = 0
check = [[False for i in range(n)] for j in range(n)]
def dfs(col, row): #(col, row) : coordination of starting point
    if check[col][row] == True or arr[col][row] == '0':
        return
    global houseCnt
    houseCnt += 1
    check[col][row] = True
    if col != n - 1:
        dfs(col + 1, row)
    if row != n - 1:
        dfs(col, row + 1)
    if col != 0:
        dfs(col - 1, row)
    if row != 0:
        dfs(col, row - 1)
    return


houseCnt_list = []
blockCnt = 0
for col in range(n):
    for row in range(n):
        if arr[col][row] == '1' and check[col][row] == False:
            blockCnt += 1
            dfs(col, row)
            houseCnt_list.append(houseCnt)
            houseCnt = 0

print(blockCnt)
houseCnt_list.sort()
for i in range(blockCnt):
    print(houseCnt_list[i])
