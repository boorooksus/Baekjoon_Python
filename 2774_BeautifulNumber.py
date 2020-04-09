from sys import stdin

t = int(stdin.readline())
for i in range(t):
    cnt = 0
    arr = []
    x = stdin.readline().strip()
    for j in range(len(x)):
        if x[j] not in arr:
            cnt += 1
            arr.append(x[j])
    print(cnt)
