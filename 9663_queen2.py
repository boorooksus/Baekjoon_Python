from sys import stdin

n = int(stdin.readline())
queen_list = []
coor_list = []
coor = []
num_list = [i + 1 for i in range(n)]

#체스판 좌표들을 구하는 함수
'''def getCoor(cnt):
    if cnt == 2:
        coor_list.append(coor)
        return
    for i in num_list:
        coor.append(i)
        getCoor(cnt + 1)
        coor.pop()'''


'''getCoor(0) #체스판 좌표들 리스트에 저장

#퀸을 놓는 방법 수 구하는 함수
def queen(cnt):
    if cnt == n:
        cases += len(queen_list)'''

check = [[False for col in range(n + 1)] for row in range(n + 1)]

def queen(cnt):
    if cnt == n:
        print(queen_list)
        return
    for i in range(1, n+1):
        for j in range(1, n+1):
            #해당 좌표값이 True인 경우 넘어간다
            if check[i][j]: continue
            #퀸이 움직일 수 있는 좌표 True로 바꾸기
            for x in range(1, n+1):
                for y in range(1, n+1):
                    if x == i or y == j:
                        check[x][y] = True
                    if abs(x-i) == abs(y-j):
                        check[x][y] = True
            queen_list.append([i,j])
            queen(cnt + 1)
            queen_list.pop()
            for x in range(i, n+1):
                for y in range(j, n+1):
                    if x == i or y == j:
                        check[x][y] = False
                    if abs(x-i) == abs(y-j):
                        check[x][y] = False
queen(0)
