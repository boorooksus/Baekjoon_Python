from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

s = []
n = int(stdin.readline())
for i in range(n):
    s.append(list(map(int, stdin.readline().split())))
visit = [[0 for _ in range(n)] for _ in range(n)]
ts = []
ans = 10 ** 9


def score(n):
    tss = 0
    tls = 0

    for i in range(n // 2):
        for j in range(0, i):
            tss += s[ts[i]][ts[j]] + s[ts[j]][ts[i]]
    tl = []
    for i in range(n):
        if i not in ts:
            for j in tl:
                tls += s[i][j] + s[j][i]
            tl.append(i)
    return abs(tss - tls)


def dfs(idx, level, n):
    global ans

    if level == n // 2 - 1:
        ts.append(idx)
        ans = min(ans, score(n))
        del ts[-1]
        return

    ts.append(idx)
    # === 1 =======================
    for i in range(idx + 1, n):
        dfs(i, level + 1, n)
    del ts[-1]
    return


for i in range(n):
    dfs(i, 0, n)
print(ans)

# 1: 백트래킹할 때 오름차순으로 해야 시간초과 안걸린다
    #순서가 달라도 팀 구성이 같으면 능력치는 같으므로 이러한 경우를 제거해서 시간을 절약한다.