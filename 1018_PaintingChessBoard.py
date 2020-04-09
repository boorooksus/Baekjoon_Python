from sys import stdin

def paint(col, row, color):
    color2 = 'N'
    if color == 'B':
        color2 = 'W'
    else:
        color2 = 'B'
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i - j) % 2 == 0 and board[col + i][row + j] != color:
                cnt += 1
            elif (i - j) % 2 == 1 and board[col + i][row + j] != color2:
                cnt += 1
    return cnt

n, m = map(int, stdin.readline().split())
board = []
for i in range(n):
    board.append(stdin.readline().strip())

ans = 64
for i in range(n - 7):
    for j in range(m - 7):
        cnt = paint(i, j, 'W')
        if cnt < ans:
            ans = cnt
        cnt = paint(i, j, 'B')
        if cnt < ans:
            ans = cnt
print(ans)