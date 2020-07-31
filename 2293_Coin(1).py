from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)


def runner(x, d):
    for i in coin:
        for j in range(i, x + 1):
            d[j] += d[j - i]
    return d[x]


d = [0 for _ in range(10001)]
d[0] = 1
n, k = map(int, stdin.readline().split())
coin = []
for _ in range(n):
    temp = int(stdin.readline())
    coin.append(temp)

print(runner(k, d))


# Dynamic Programming
# 나중에 다시 풀어볼 것
