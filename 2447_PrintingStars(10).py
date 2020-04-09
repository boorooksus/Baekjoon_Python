from sys import stdin, setrecursionlimit
from math import log

setrecursionlimit(10 ** 9)

def recursion(k, col, row):
    if k == 0:
        board[col][row] = '*'
        return

    size = 3 ** k
    recursion(k - 1, col, row)
    # == 2 ==
    recursion(k - 1, col, row + size // 3)
    recursion(k - 1, col, row + size // 3 * 2)
    recursion(k - 1, col + size // 3, row)
    recursion(k - 1, col + size // 3, row + size // 3 * 2)
    recursion(k - 1, col + size // 3 * 2, row)
    recursion(k - 1, col + size // 3 * 2, row + size // 3)
    recursion(k - 1, col + size // 3 * 2, row + size // 3 * 2)

    return

n = int(stdin.readline())
#== 1 ==
k = int(round(log(n, 3), 0))
board = [[' ' for i in range(n)] for j in range(n)]
recursion(k, 0, 0)

for i in range(n):
    for j in range(n):
        print(board[i][j], end='')
    print()

#분할 정복 알고리즘
#1 : 로그 사용법, round 사용법
    #log만 사용하면 실수 오차 때문에 243 넣었을 때 5가 아니라 4가 나옴
#2 : 재귀함수에 시작지점 넣을 때 col, row에 더하는 것 잊으면 안됨

#재귀 안쓰는 법 : https://hwiyong.tistory.com/213