from sys import stdin

n, k = map(int, stdin.readline().split())
coin = []
cnt = 0
#cur = k
#isPrinted = False
for i in range(n):
    coin.append(int(stdin.readline()))

# ==== 1 ==============================
'''for i in range(n - 1, -1, -1):
    while 1:
        cur += coin[i]
        cnt += 1
        if cur > k:
            cur -= coin[i]
            cnt -= 1
            break
        elif cur == k:
            print(cnt)
            isPrinted = True
            break
    if isPrinted == True:
        break'''

for i in range(n-1, -1, -1):
    cnt += k // coin[i]
    if k % coin[i] == 0:
        print(cnt)
        break
    else:
        k = k % coin[i]

# 그리디 알고리즘
# 1 : 이렇게 쓸데없이 for문 안에 while문 써서 시간초과