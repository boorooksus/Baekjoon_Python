from collections import deque
from sys import stdin


t = int(stdin.readline())
for _ in range(t):
    p = stdin.readline().strip()
    n = int(stdin.readline())
    temp = stdin.readline().strip()
    if n == 0:
        arr_str = []
    else:
        arr_str = temp[1:-1].split(",")
    arr = deque()
    for i in arr_str:
        arr.append(int(i))

    is_err = 0
    is_r = 0
    for i in p:
        if i == 'R':
            is_r = (is_r + 1) % 2
        elif i == 'D' and len(arr) == 0:
            is_err = 1
            break
        else:
            if is_r == 1:
                arr.pop()
            else:
                arr.popleft()
    if is_err == 1:
        print('error')
    elif len(arr) == 0:
        print('[]')
    elif is_r == 1:
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            ans.append(arr[i])
        print("[", end='')
        for i in ans[:-1]:
            print(i, end=',')
        print(ans[-1], end=']')
        print('')

    else:
        ans = []
        for i in arr:
            ans.append(i)
        print("[", end='')
        for i in ans[:-1]:
            print(i, end=',')
        print(ans[-1], end=']')
        print('')


# 출력 결과에서 배열 원소 사이에 띄어쓰기 있어서 틀림.
# 배열에 원소가 없을 때, 출력하면 에러뜸 -> 별도로 케이스 관리