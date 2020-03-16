from sys import stdin

n, m = map(int, stdin.readline().split())
sequence = []
check = [False] * (n + 1)

def getNum(cnt):
    if cnt == m:
        '''if sorted(sequence) == sequence:
            print(*sequence)'''
        print(*sequence)
        return

    for i in range(1, n + 1):
        if not check[i]:
            check[i] = True
            sequence.append(i)
            getNum(cnt + 1)
            sequence.pop()
            #check[i] = False
            for j in range(i + 1 , n + 1):
                check[j] = False

getNum(0)