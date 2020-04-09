from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

cnt = [0, 0, 0]

def nop(n, col, row):

    color = arr[col][row]
    isSame = True
    for i in range(n):
        for j in range(n):
            if arr[col + i][row + j] != color:
                isSame = False

        if isSame == False:
            nop(n // 3, col, row)
            nop(n // 3, col, row + n // 3)
            nop(n // 3, col, row + n // 3 * 2)
            nop(n // 3, col + n // 3, row)
            nop(n // 3, col + n // 3, row + n // 3)
            nop(n // 3, col + n // 3, row + n // 3 * 2)
            nop(n // 3, col + n // 3 * 2, row)
            nop(n // 3, col + n // 3 * 2, row + n // 3)
            nop(n // 3, col + n // 3 * 2, row + n // 3 * 2)
            return
    if isSame == True:
        if color == -1:
            cnt[0] += 1
            return
        elif color == 0:
            cnt[1] += 1
            return
        else:
            cnt[2] += 1
            return

nop(n, 0, 0)
for i in range(3):
    print(cnt[i])



#분할 정복
