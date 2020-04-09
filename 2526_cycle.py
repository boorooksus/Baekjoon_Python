from sys import stdin

n, p = map(int, stdin.readline().split())

arr = []
x = n
idx = 0
while 1:
    x = (x * n) % p
    if x in arr:
        idx = arr.index(x)
        break
    arr.append(x)

print(len(arr) - idx)