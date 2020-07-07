from sys import stdin


def mysort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) -(i + 1)):
            a = arr[j + 1]
            if a < 0:
                a *= -1
            b = arr[j]
            if b < 0:
                b *= -1
            if a < b:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
            elif a == b and arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr

arr = []
n = int(stdin.readline())
for i in range(n):
    x = int(stdin.readline())

    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            arr = mysort(arr)
            print(arr[0])
            del arr[0]

    else:
        arr.append(x)


# 시간 초과