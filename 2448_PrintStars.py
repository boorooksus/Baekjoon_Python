from sys import stdin, setrecursionlimit
from math import log
setrecursionlimit(10**9)

n = int(stdin.readline())
k = int(log(n // 3, 2))

table = [[' ' for i in range((2 ** k) * 6 - 1)] for j in range((2 ** k) * 3)]

#재귀 통해 별 찍기
#phase : 삼각형 단계(0단계가 최소), col : 삼각형 위 꼭지점위치의 행, row : 삼각형 위 꼭지점 위치의 열
def stars(phase, col, row):
    #0단계(재귀의 마지막)일 때 별을 삼각형으로 저장한다.
    if phase == 0:
        table[col][row] = '*'
        table[col + 1][row - 1] = '*'
        table[col + 1][row + 1] = '*'
        for i in range(3):
            table[col + 2][row - i] = '*'
            table[col + 2][row + i] = '*'
        return
    #재귀함수 3번 사용- 맨 위 꼭지점, 왼쪽 중간 꼭지점, 오른쪽 중간 꼭지점에서 시작하는
    #한 단계 작은삼각형 만들도록
    stars(phase - 1, col, row)
    stars(phase - 1, col + (2 ** (phase - 1) * 3), row - ((2 ** (phase - 1)) * 3))
    stars(phase - 1, col + (2 ** (phase - 1) * 3), row + ((2 ** (phase - 1)) * 3))

    return

stars(k, 0, (2 ** k) * 3 - 1)

for i in range(len(table)):
    #line_str = ''.join(table[i])
    print(''.join(table[i]))

'''for i in range(len(table)):
    for j in range(len(table[i])):
        print(table[i][j], end='')
    print()'''


#1. 24~25 번째 줄 phase를 k로 써서 틀림 -> 확인 잘 할 것
#2. 출력 때 문자 하나하나 출력하면 시간초과 뜸
# -> 문자열로 출력하니 통과
#3. 리스트를 문자열로 변환하는 법 기억하기
#4. 8번째 줄 뒤쪽에 range안 써서 시간 날림