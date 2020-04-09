from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
isDone = False

def sudoku(idx):
    # ==== 1 =========
    global isDone
    if isDone == True:
        return

    if idx == len(blank):
        for k in range(9):
            print(*board[k])
        isDone = True
        return

    col = blank[idx][0]
    row = blank[idx][1]

    candi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if board[col][i] in candi:
            candi.remove(board[col][i])
        if board[i][row] in candi:
            candi.remove(board[i][row])
    for i in range((col // 3) * 3, (col // 3) * 3 + 3):
        for j in range((row // 3) * 3, (row // 3) * 3 + 3):
            if board[i][j] in candi:
                candi.remove(board[i][j])

    for i in candi:
        board[col][row] = i
        sudoku(idx + 1)
        board[col][row] = 0

    return

blank = []
board = [[int(x) for x in stdin.readline().split()] for y in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])

sudoku(0)

#이전 버전 참고
