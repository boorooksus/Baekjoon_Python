from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(stdin.readline())
h = list(map(int, stdin.readline().split()))
sortedh = h[:]
sortedh.sort(reverse=True)
cnt = 0


def arrow(height, start):
    global isPoped
    if height in h[start:]:
        idx = h[start:].index(height) + start
        del h[idx]
        sortedh.remove(height)
        isPoped = True
        arrow(height - 1, idx)

    return


for height in sortedh:
    isPoped = False
    arrow(height, 0)
    if isPoped == True:
        cnt += 1

print(cnt)
