from sys import stdin
import queue

n, m = map(int, stdin.readline().split())
order = [[0] for i in range(n + 1)]
inDegree = [0 for i in range(n + 1)]
q = queue.Queue()

def topologySort():
    result = []
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            q.put(i)
    for i in range(1, n + 1):
        x = q.get()
        result.append(x)
        for j in range(1, len(order[x])):
            y = order[x][j]
            inDegree[y] -= 1
            if inDegree[y] == 0:
                q.put(y)

    print(*result)


for i in range(m):
    a, b = map(int, stdin.readline().split())
    order[a].append(b)
    inDegree[b] += 1

topologySort()