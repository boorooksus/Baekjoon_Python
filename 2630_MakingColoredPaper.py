from sys import stdin

n = int(stdin.readline())
paper = []
for i in range(n):
    paper.append(list(map(int, stdin.readline().split())))
acnt = 0 #흰색 종이 개수
bcnt = 0 #파란색 종이 개수

def cp(n, col, row):
    global acnt
    global bcnt
    #======= 1 ==================================
    #만약 모두 0이면 하얀색 종이 완성
    isDone = True
    for i in range(n):
        #======= 2 =====================================
        if 1 in paper[col + i][row:row + n]:
            isDone = False
            break
    if isDone == True:
        acnt += 1
        return
    #만약 모두 1이면 파란색 종이 완성
    isDone = True
    for i in range(n):
        if 0 in paper[col + i][row:row + n]:
            isDone = False
            break
    if isDone == True:
        bcnt += 1
        return

    #모든 숫자가 같은 종이 나올때까지 분할하여 재귀
    cp(n // 2, col, row)
    cp(n // 2, col + (n // 2), row)
    cp(n // 2, col, row + (n // 2))
    cp(n // 2, col + (n // 2), row + (n // 2))
    return

cp(n, 0, 0)

print(acnt)
print(bcnt)


#분할 정복 알고리즘
# 1 : 2차원 리스트 인덱스 슬라이싱 아래처럼 했다가 틀림
'''if 0 not in paper[col:col + n - 1][row:row + n - 1]\
        and paper
        acnt += 1
        return
    if 1 not in paper[col:col + n - 1][row:row + n - 1]:
        acnt += 1
        return'''
#2 : row의 인덱스 슬라이싱 범위 아래처럼 잘못 잡았다가 틀림
    # if 1 in paper[col + i][row:row + n - 1]

