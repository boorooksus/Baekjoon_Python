from sys import stdin

def upperbound(cur, n):
    start = 0
    end = n - 1
    while(start < end):
        mid = start + (end - start) // 2
        if cur <= x[mid]:
            end = mid
        else:
            start = mid + 1
    return x[start]


n, c = map(int, stdin.readline().split())

x = []

for i in range(n):
    x.append(int(stdin.readline()))

x.sort()
if (x[-1] - x[0]) % c == 0:
    space = (x[-1] - x[0]) // c
else:
    space = (x[-1] - x[0]) // c + 1

router = []
router.append(x[0])
ans  = 1000000000
for i in range(1, c):
    cur = router[-1] + space
    router.append(upperbound(cur, n))
    if router[i] - router[i - 1] < ans:
        ans = router[i] - router[i - 1]

print(ans)
