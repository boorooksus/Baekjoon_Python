from sys import stdin


n, c = map(int, stdin.readline().split())

x = []

for i in range(n):
    x.append(int(stdin.readline()))

x.sort()

ans = 0
start, end = 1, x[-1] - x[0]
while start <= end:  # == 1 ==============================
    mid = (start + end) // 2
    cnt = 1
    cur = x[0]
    for i in x:
        if i >= cur + mid:
            cnt += 1
            cur = i

    if cnt >= c:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1  # == 1 ========================

print(ans)

# 이분탐색
# 1: 15줄의 '<=' 대신 '<'쓰고 29줄에 'end = mid'로 쓰면 틀렸다고 나옴