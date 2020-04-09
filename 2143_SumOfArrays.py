from sys import stdin

zero = [0]
t = int(stdin.readline())
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
a = zero + a
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))
b = zero + b

#a.sort()
#b.sort()

aStart = 0
aEnd = 0
bStart = 0
bEnd = 0
aSum = a[0]
bSum = b[0]
cnt = 0
print("a : ", a)
print("b : ", b)

while aEnd < n:
    aEnd += 1
    aSum += a[aEnd]

    while aSum > t - b[1]:
        aSum -= a[aStart]
        aStart += 1

    while bEnd < m:
        bEnd += 1
        bSum += b[bEnd]
        if(aStart == 2 and aEnd == 2):
            print("HI!")

        while aSum + bSum > t:
            bSum -= b[bStart]
            bStart += 1

        if aSum + bSum == t:
            print("as:", aStart, "ae:", aEnd, "bs:", bStart, "be:", bEnd)
            print("aSum:", aSum, "bSum:", bSum)
            cnt += 1

    bStart = 0
    bEnd = 0
    bSum = b[bStart]


print(cnt)