from sys import stdin

n, m = map(int, stdin.readline().split())
square = []
'''for i in range(n):
    line = int(stdin.readline())
    square.append(list(int(j) for j in str(line)))'''
for i in range(n):
    square.append(stdin.readline())

size = min(n, m)
ans = 1
'''for i in range(size, 0, -1):
    for j in range(n - i + 1):
        for k in range(m - i + 1):
            if square[j][k] == square[j][k + i - 1] \
                    and square[j][k + i - 1] == square[j + i - 1][k + i - 1]\
                    and square[j + i - 1][k + i - 1] == square[j + i - 1][k]:
                if ans < i * i:
                    ans = i * i
                    break
            if ans > 1:
                break
        if ans > 1:
            break'''
for i in range(1, size):
    for j in range(n - i):
        for k in range(m - i):
            a = int(square[j][k])
            b = int(square[j][k + i])
            c = int(square[j + i][k + i])
            d = int(square[j + i][k])
            if a == b and b == c and c == d and ans < (i + 1) ** 2:
                ans = (i + 1) ** 2


print(ans)