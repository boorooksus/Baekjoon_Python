from sys import stdin

n, m = map(int, stdin.readline().split())

sequence = []

def get(cnt):
    if cnt == m:
        print(*sequence)
        return

    for i in range(1, n + 1):
        sequence.append(i)
        get(cnt + 1)
        sequence.pop()
get(0)