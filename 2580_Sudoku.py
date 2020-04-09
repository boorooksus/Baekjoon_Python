from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
isDone = False #수도쿠 완성됐는지

def sudoku(idx):
    # ==== 1 =========
    global isDone
    if isDone == True:
        return

    #빈칸의 개수만큼 재귀하여 채웠으면 프린팅
    if idx == len(blank):
        for k in range(9):
            print(*board[k])
        isDone = True
        return

    col = blank[idx][0]
    row = blank[idx][1]
    # 빈 칸에 들어갈 수 있는 후보들을 추려낸다
    candi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        candi[board[col][i]] = 0
        candi[board[i][row]] = 0
    for i in range((col // 3) * 3, (col // 3) * 3 + 3):
        for j in range((row // 3) * 3, (row // 3) * 3 + 3):
            candi[board[i][j]] = 0

    for i in range(1, 10):
        if candi[i] != 0:
            board[col][row] = candi[i]
            sudoku(idx + 1)
            # === 2===========
            board[col][row] = 0

    return

blank = []
board = [[int(x) for x in stdin.readline().split()] for y in range(9)]
# === 3 =====================
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])

sudoku(0)

#백트래킹
#Phthon3로 재출하면 시간초과, pypy3로 제출하면 통과
# 1 : 이미 한 번이라도 프린팅 되었으면 리턴시키자
# 2 : 재귀 함수 빠져나오면 0으로 바꾸자 그래야 후보 틀리고 다음 후보로 넘어갔을 때
    #제대로 된다. ex)
'''0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0'''
    #이거 입력했을 때
# 3 : [[i, j] for i in range(9) for j in range(9) if board[i][j] == 0]
    #이런식으로도 바꿀 수 있음
