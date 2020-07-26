from sys import stdin

dsp = [0 for _ in range(1000)]
dep = [0 for _ in range(1000)]

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

sp = 0
ep = 0

dsp[0] = 1
dep[n - 1] = 1

for i in range(n):
    for j in range(i - 1, -1, -1):
        # ==== 1 ========================================
        if a[j] < a[i] and dsp[j] >= dsp[i]:
            dsp[i] = dsp[j] + 1
        if a[n - i - 1] > a[n - j - 1] and dep[n - i - 1] <= dep[n - j - 1]:
            dep[n - i - 1] = dep[n - j - 1] + 1
    # ========= 2 ========================================
    if dsp[i] == 0:
        dsp[i] += 1
    if dep[n - i - 1] == 0:
        dep[n - i - 1] += 1


ans = 0
idx = 0
for i in range(n):
    if ans < dsp[i] + dep[i] - 1:
        ans = dsp[i] + dep[i] - 1
        idx = i

print(ans)


# 동적 프로그래밍
# 1 : 조건에 맞는 가장 최신의 것인지 확인하기 위해
    # dsp[j] >= dsp[i] 이 조건 있어야 함. 등호도 꼭 붙여야함
# 2 : 자기보다 작은 수가 없는 경우에는 1로 바꿔줘야함

