from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


p = 1000000007
def multi(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y % 2 == 1:
        #return (x * (multi(x, y // 2) ** 2) % p) % p
        return (x * multi(x, y - 1)) % p
    else:
        return (multi(x, y // 2) ** 2) % p


n, k = map(int, stdin.readline().split())

a = 1
for i in range(1, n + 1):
    a *= i
    a %= p
b = 1
for i in range(1, k + 1):
    b *= i
    b %= p
for i in range(1, n - k + 1):
    b *= i
    b %= p
b = multi(b, p - 2)
print((a * b) % p)


#페르마의 소정리, 분할 정복
