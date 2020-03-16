from sys import stdin

n = int(stdin.readline().split())
queen = [] #퀸의 좌표
queens_list = [] #퀸의 좌표들을 저장
x_check = [False] * (n + 1)
y_check = [False] * (n + 1)
num_list = [i + 1 for i in range(n)]

def get(cnt):
    '''if cnt == 2:
        queens_list.append(queen)
        return

    for i in num_list:
        if check[i]: continue

        check[i] = True
        queen.append(i)
        get(cnt + 1)'''
    for i in num_list:
        if x_check[i]: continue
        #x좌표 구하기
        x_check[i] = True
        queen.append(i)

        for j in num_list:
            if y_check[j]: continue
            #y좌표 구하기
            y_check[j] = True
            queen.append(j)
            #퀸의 좌표를 리스트에 넣는다
            queens_list.append(queen)
            #퀸이 들어갈 수 없는 좌표들 구하기
            

#마지막에 total C n 구할 것