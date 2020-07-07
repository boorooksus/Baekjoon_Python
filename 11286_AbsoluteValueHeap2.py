from sys import stdin


arr = []
n = int(stdin.readline())
for i in range(n):
    x = int(stdin.readline())

    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            arr.sort()
            temp = arr[0][0] * arr[0][1]
            print(temp)
            del arr[0]

    else:
        sign = 1
        if x < 0:
            x *= -1
            sign = -1

        arr.append((x, sign))


# 시간 초과