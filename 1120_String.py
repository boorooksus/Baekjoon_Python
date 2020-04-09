from sys import stdin

a, b = stdin.readline().split()
gap = len(b) - len(a)
ans = 100000

for i in range(gap + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i +j]:
            cnt += 1
    if cnt < ans:
        ans = cnt


print(ans)