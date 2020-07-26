from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

s = []
n = int(stdin.readline())
for i in range(n):
    s.append(list(map(int, stdin.readline().split())))
visit = [0 for _ in range(n)]
ts = []
ans = 10 ** 9



def dfs(idx, level, n, tss):
    global ans

    if visit[idx] != 0:
        return
    if level == n // 2 - 1:
        for i in ts:
            tss += s[idx][i] + s[i][idx]
        visit[idx] = 1
        tl = []
        tls = 0
        for i in range(n):
            if visit[i] == 0:
                for j in tl:
                    tls += s[i][j] + s[j][i]
                tl.append(i)
                visit[i] = 1
        for i in tl:
            visit[i] = 0
        ans = min(ans, abs(tss - tls))
        visit[idx] = 0
        return

    for i in ts:
        tss += s[i][idx] + s[idx][i]
    visit[idx] = 1
    ts.append(idx)
    for i in range(n):
        dfs(i, level + 1, n, tss)
    visit[idx] = 0
    del ts[-1]
    return

for i in range(n):
    dfs(i, 0, n, 0)
print(ans)