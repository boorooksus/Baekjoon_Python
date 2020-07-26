from sys import stdin

ans = []
arr = []
n, k = map(int, stdin.readline().split())
for i in range(n):
    arr.append(i + 1)
cur = 0
while(arr):
    cur = (cur + (k - 1)) % len(arr)
    ans.append(arr[cur])
    del arr[cur]
print("<", end='')
for i in ans[:-1]:
    print("%s, "%i, end='')
print("%s>"%ans[-1])
