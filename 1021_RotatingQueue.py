from sys import stdin


n, m = map(int, stdin.readline().split())
target = list(map(int, stdin.readline().split()))
arr = [i+1 for i in range(n)]
cnt = 0
cur = 0
for i in range(m):
    idx = arr.index(target[i])
    cnt += min(abs(idx - cur), min(abs(len(arr) + cur - idx), abs(len(arr) + idx - cur)))
    del arr[idx]
    cur = idx

print(cnt)