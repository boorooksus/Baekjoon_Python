from sys import stdin

n = int(stdin.readline())
time = list(map(int, stdin.readline().split()))

time.sort()

# == 1 ==
ans = 0
for i in range(n):
    ans += (n - i) * time[i]

print(ans)

# 1 : 그리디 알고리즘으로도 풀어보면
    #waiting_time = 0
    #total_time = 0
    #for i in time:
    #    waiting_time += i
    #    total_time += waiting_time