from sys import stdin


def R(arr):
    temp = []
    for i in range(len(arr) - 1, -1, -1):
        temp.append(arr[i])
    return temp


def D(arr):
    temp = arr
    del temp[0]
    return temp


t = int(stdin.readline())
for _ in range(t):
    p = stdin.readline().strip()
    n = int(stdin.readline())
    temp = stdin.readline().strip()
    if n == 0:
        print('error')
        continue
    arr_str = temp[1:-1].split(",")
    arr = list(int(i) for i in arr_str)

    is_err = 0
    for i in p:
        if i == 'R':
            arr = R(arr)
        elif i == 'D' and len(arr) == 0:
            is_err = 1
            break
        else:
            arr = D(arr)
    if is_err == 1:
        print('error')
    else:
        print(arr)