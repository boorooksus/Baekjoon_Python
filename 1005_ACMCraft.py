from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)
import queue

result = 0
q = queue.Queue()

#w가 나올때까지 재귀(w 전에 outDegree가 0이되면 -1리턴)
def topologySort(start, w, cnt, n):
    if time_list[start] != 0:
        return time_list[start]

    if start == w:
        return d_dict[w]
    #사이클이 발생하거나 w이전에 outDegree가 0이 되면 -1 리턴
    if cnt > n or len(order[start]) == 0:
        time_list[start] = -1
        return -1

    x = -1
    for i in range(len(order[start])):
        y = topologySort(order[start][i], w, cnt + 1, n)
        if x < y:
            x = y
    if x == -1:
        time_list[start] = -1
        return -1
    time_list[start] = d_dict[start] + x
    return d_dict[start] + x


t = int(stdin.readline()) #t : test cases
for i in range(t):
    #n : number of buildings, k : number of construction orders
    n, k = map(int, stdin.readline().split())
    order = [[] for a in range(n + 1)]
    inDegree = [0 for b in range(n + 1)]
    #d : cost to build each buildings
    d_list = list(map(int, stdin.readline().split()))
    d_dict = {c + 1:d_list[c] for c in range(n)}
    for j in range(k):
        #x, y : construction order(x->y)
        x, y = map(int, stdin.readline().split())

        order[x].append(y)
        inDegree[y] += 1
    #w : building number construction needed to win
    w = int(stdin.readline())
    time_list = [0 for i in range(n + 1)]  #w까지 건설하는데 드는 시간 저장
    ans = -1
    for d in range(1, n+1):
        if inDegree[d] == 0:
            result = topologySort(d, w, 0, n)
            if ans < result:
                ans = result
    print(ans)

