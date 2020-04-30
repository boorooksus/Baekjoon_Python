from sys import stdin


d = [0 for _ in range(100000)]

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))

d[0] = num[0]
ans = d[0]

for i in range(1, n):
    if i == 8:
        here = 0
    if d[i - 1] + num[i] < num[i]:
        d[i] = num[i]
    else:
        d[i] = d[i - 1] + num[i]
    if ans < d[i]:
        ans = d[i]

print(ans)

