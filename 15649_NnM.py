from sys import stdin

n, m = map(int, stdin.readline().split())
sequence = []
check = [False] * (n + 1)

def getNum(cnt):
    if cnt == m:
        print(*sequence)
        return

    for i in range(1, n + 1):
        if not check[i]:
            check[i] = True
            sequence.append(i)
            getNum(cnt + 1)
            sequence.pop()
            check[i] = False

getNum(0)