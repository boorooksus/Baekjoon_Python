from sys import stdin

n, m = map(int, stdin.readline().split())

sequence = []
check = [False] * (n + 1)
num_list = [i + 1 for i in range(n)]

def get(cnt):
    if cnt == m:
        print(*sequence)
        return

    for i in num_list:
        if not check[i]:
            for j in range(1, i):
                check[j] = True
            sequence.append(i)
            get(cnt + 1)
            sequence.pop()
            for k in range(i, n + 1):
                check[k] = False

get(0)