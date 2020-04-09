from sys import stdin, stdout

n = int(stdin.readline())

def check(col, row):
    i = col
    j = row
    while(i < n or j < n):
        if col < n:
            check_list[i][row] = True
        if row < n:
            check_list[col][j] = True
        if col < n and row < n:
            check_list[i][j] = True
        i += 1
        j += 1

check_list = [[False for a in range(n)] for b in range(n)]
for i in range(n):
    for j in range(n):
        if check_list[i][j] == False:
            check(i, j)