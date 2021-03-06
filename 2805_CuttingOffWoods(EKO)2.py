from sys import stdin

def cutWood(x):
    sum = 0
    for i in h:
        if i - x > 0:
            sum += i - x
    return sum


n, m = map(int, stdin.readline().split())
h = list(map(int, stdin.readline().split()))

h.sort()

start, end = -1, h[-1] + 1
while start <= end:
    mid = (start + end) // 2
    if cutWood(mid) >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)


# 이분탐색