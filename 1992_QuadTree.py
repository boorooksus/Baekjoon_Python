from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(stdin.readline())
arr = []
#===== 1===================
for i in range(n):
    arr.append(stdin.readline())

def qt(n, col, row):
    isDone = True
    for i in range(n):
        if '1' in arr[col + i][row: row + n]:
            isDone = False
            break
    if isDone == True:
        print('0', end='')
        return

    isDone = True
    for i in range(n):
        if '0' in arr[col + i][row: row + n]:
            isDone = False
            break
    if isDone == True:
        print('1', end='')
        return

    print('(', end='')
    qt(n // 2, col, row)
    qt(n // 2, col, row + n // 2)
    qt(n // 2, col + n // 2, row)
    qt(n // 2, col + n // 2, row + n // 2)
    print(')', end='')

    return

qt(n, 0, 0)


#분할 정복
#2630번이랑 유형이랑 거의 같음
# 1 : string 말고 list로 저장하고 싶을 땐 아래와 같이 쓰면 됨
'''for _ in range(N):
    matrix.append(list(map(int, str(input()))))'''