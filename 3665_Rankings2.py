from sys import stdin
import queue

t = int(stdin.readline()) #test cases

def topologySort(n, m):
    for j in range(m):
        #A pair of teams whose rank has changed
        a, b = map(int, stdin.readline().split())
        #간선관계가 a -> b 로 바뀌도록 해야하는지 확인
        if lastRanking.index(a) < lastRanking.index(b):
            temp = a
            a = b
            b = temp
        #간선관계를 a->b로 바꾼다
        order[a].append(b)
        inDegree[b] += 1
        order[b].remove(a)
        inDegree[a] -= 1
    for j in range(1, n + 1):
        if inDegree[j] == 0:
            q.put(j)
    for j in range(1, n + 1):
        #사이클이 있는 경우
        if q.empty():
            print("IMPOSSIBLE")
            return
        x = q.get()
        result.append(x)
        #순위가 확실치 않을 때
        if not q.empty():
            print('?')
            return
        for k in range(len(order[x])):
            y = order[x][k]
            inDegree[y] -= 1
            if inDegree[y] == 0:
                q.put(y)
    print(*result)
    return

for i in range(t):
    result = []
    q = queue.Queue()
    n = int(stdin.readline()) #number of teams
    order = [[] for i in range(n + 1)]
    inDegree = [0 for i in range(n + 1)]
    #the rankings for last year
    lastRanking = list(map(int, stdin.readline().split()))
    #작년 순위를 그래프로 저장
    for j in range(0, n):
        for k in range(j + 1, n):
            order[lastRanking[j]].append(lastRanking[k])
            inDegree[lastRanking[k]] += 1

    # number of teams whose rank has changed from last year
    m = int(stdin.readline())
    topologySort(n, m)