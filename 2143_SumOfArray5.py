from sys import stdin

t = int(stdin.readline())
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

aSum = []
bSum = []

for start in range(n):
    sum = 0
    for end in range(start, n):
        sum += a[end]
        aSum.append(sum)

for start in range(m):
    sum = 0
    for end in range(start, m):
        sum += b[end]
        bSum.append(sum)

#이진 탐색 위해서 정렬
aSum.sort()
bSum.sort()

cnt = 0
#== 1 ==
for x in aSum:
    y = t - x
    cnt += bSum.count(y)

print(cnt)

#딕셔너리 안쓴 방법으로 시도
#이진탐색 사용
#1 : 여기서 시간초과
    #c++에선 upper bound, lower bound 사용하여 count 얻을 수있음
    #여기선 그게 없어서 count()함수 썼다가 시간초과