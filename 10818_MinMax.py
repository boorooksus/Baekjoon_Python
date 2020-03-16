n = int(input())
a = list(map(int, input().split()))
min_ = 1000000
max_ = -1000000
for i in range(n):
    if min_ > a[i]:
        min_ = a[i]
    if max_ < a[i]:
        max_ = a[i]
print(min_, max_)