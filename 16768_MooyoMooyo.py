from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

def dfs(col, row, color, cnt):
    if board[col][row] != color:
        return 0
    if check[col][row] == 1:
        return 0

    check[col][row] = 1
    cnt += 1
    if col > 0:
        cnt += dfs(col - 1, row, color, cnt)
    if col < n - 1:
        cnt += dfs(col + 1, row, color, cnt)
    if row > 0:
        cnt += dfs(col, row - 1, color,cnt )
    if row < n - 1:
        cnt += dfs(col, row + 1, color, cnt)

    return cnt

def rmv(col, row, color):
    if board[col][row] != color:
        return
    if check[col][row] == 1:
        return

    check2[col][row] = 1
    board[col][row] = 0
    if col > 0:
        rmv(col - 1, row, color)
    if col < n - 1:
        rmv(col + 1, row, color)
    if row > 0:
        rmv(col, row - 1, color)
    if row < n - 1:
        rmv(col, row + 1, color)

    return

def arrange():
    for row in range(10):
        for col in range(n - 1, -1, -1):
            if board[col][row] == 0:
                del board[col][row]
                board[col].insert(0, 0)

n, k = map(int, stdin.readline().split())
board = []
for i in range(n):
    board.append(map(int, stdin.readline().split()))

isDone = False
while(isDone == False):
    isDone = True
    check = [[0 for i in range(10)] for j in range(n)]
    check2 = [[0 for i in range(10)] for j in range(n)]

    for col in range(n):
        for row in range(10):
            if board[col][row] == 0 or check[col][row] == 1:
                continue
            color = board[col][row]
            cnt = 0
            if dfs(col, row, color, cnt) >= k:
                rmv(col, row, color)
            isDone = False
            arrange()

for i in range(n):
    print(*board[col])