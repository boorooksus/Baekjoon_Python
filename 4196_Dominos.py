from sys import stdin

'''def getParent(x):
    if parent_list[x] == x:
        return x
    result = getParent(parent_list[x])
    return result

def unionParent(x, y):
    x = getParent(x)
    y = getParent(y)
    if x != y:
        parent_list[y] = x'''

def dfs(x):
    global id
    id += 1
    d[x] = id
    stack.append(x)

    parent = d[x]
    for i in range(len(a[x].size())):
        y = a[x][i]
        #탐색 안 된 노드일때
        if d[y] == 0:
            parent = min(parent, dfs(y))
        #아직 처리중인 이웃일 때
        elif finished[y] == False:
            parent = min(parent, d[y])

    #부모가 자기자신일 때
    if parent == d[x]:
        scc = []
        while(1):
            t = stack[-1]
            stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)


t = int(stdin.readline()) #t : test cases
for i in range(t):
    #n : number of dominos, m : number of lines that shows rule
    n, m = map(int, stdin.readline().split())
    d = [0 for i in range(n + 1)]
    id = 0
    a = [[] for i in range(n + 1)]
    b = [[] for i in range(n + 1)]
    stack = []
    finished = [False for i in range(n + 1)]
    SCC = []
    inDegree = [0 for i in range(n + 1)]
    for j in range(m):
        x, y = map(int, stdin.readline().split())
        a[x].append(y)
        b[y].append(x)
        inDegree[y] += 1
    for j in range(1, n + 1):
        if d[j] == 0:
            dfs(j)
    cnt = len(SCC)
    check = [False] * cnt
    for j in range(cnt):
        if SCC[i] == False:
            size = len(SCC[i])
            for k in range(size):
                
