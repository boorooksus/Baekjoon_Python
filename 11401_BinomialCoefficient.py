from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


def factorial(x, y):
    if y == 1:
        return x

    if y % 2 == 1:
        return (x * (factorial(x - 1, (y - 1) // 2)) * (
            factorial(x - 1 - (y - 1) // 2, (y - 1) // 2)))
    else:
        return factorial(x, y // 2) * factorial(x - (y // 2), y // 2)


n, k = map(int, stdin.readline().split())

if k > n - k:
    k = n - k

if k == 0:
    print(n % 1000000007)
else:
    a = factorial(n, k)
    b =  factorial(k, k)
    # == 1=========================
    print((a // b) % 1000000007)


#시간초과
# 1 : MOD는 나눗셈에선 분배법칙 성립 X