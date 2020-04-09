from sys import stdin

zero = [0]
t = int(stdin.readline())
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
a = zero + a
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))
b = zero + b

aStart = 0
aEnd = 0
bStart = 0
bEnd = 0
aSum = a[0]
bSum = b[0]
cnt = 0

while aEnd < n:
    aEnd += 1
    aSum += a[aEnd]

    aStart = 0
    aSum = 0
    for i in range(aEnd + 1):
        aSum += a[i]

    while aStart <= aEnd:
        while bEnd < m:
            bEnd += 1
            bSum += b[bEnd]

            bStart = 0
            bSum = 0
            for j in range(bEnd + 1):
                bSum += b[j]

            while bStart <= bEnd:
                if aSum + bSum == t and aStart != 0 and bStart != 0:
                    cnt += 1
                bSum -= b[bStart]
                bStart += 1

        aSum -= a[aStart]
        aStart += 1
        bEnd = 0

print(cnt)

#시간초과