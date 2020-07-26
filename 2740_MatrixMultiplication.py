from sys import stdin

n, m = map(int, stdin.readline().split())
a = []
for i in range(n):
    #line = list(stdin.readline().split())
    #a.append(list(int(i) for i in line))
    a.append(list(map(int, stdin.readline().split())))
m, k = map(int, stdin.readline().split())
b = []
for i in range(m):
    #line = list(stdin.readline().split())
    #b.append(list(int(i) for i in line))
    b.append(list(map(int, stdin.readline().split())))
ans = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            ans[i][j] += a[i][x] * b[x][j]
for i in range(n):
    print(*ans[i])