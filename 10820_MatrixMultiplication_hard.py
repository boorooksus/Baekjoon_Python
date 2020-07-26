from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

mod = 1000
n, b = map(int, stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, stdin.readline().split())))


def multi(x, y):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] = (ans[i][j] + (x[i][k] * y[k][j]) % mod) % mod
    return ans


def square(x, y):
    if y == 0:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            ans[i][i] = 1
        return ans
    elif y == 1:
        for i in range(n):
            for j in range(n):
                x[i][j] %= mod
        return x

    if y % 2 == 1:
        return multi(x, square(x, y - 1))
    else:
        temp = square(x, y // 2)
        return multi(temp, temp)


ans = square(a, b)
for i in range(n):
    print(*ans[i])
