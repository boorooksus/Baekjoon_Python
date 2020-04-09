from sys import stdin

INF = 10000001
#number of cities
n = int(stdin.readline())
graph = [[0 if i == _ else INF for i in range(n + 1)] for _ in range(n + 1)]
#number of buses
m = int(stdin.readline())

for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    # === 1 =============
    if graph[a][b] > c:
        graph[a][b] = c

def bfs():
    for stop in range(1, n + 1):
        for start in range(1, n + 1):
            for des in range(1, n + 1):
                if graph[start][des] >\
                    graph[start][stop] + graph[stop][des]:
                    graph[start][des] = graph[start][stop] +\
                        graph[stop][des]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                graph[i][j] = 0
            print(graph[i][j], end=' ')
        print()


bfs()

#플로이드 와샬
# 1 : 같은 경로에 길 여러개 일수도 있음 -> 제일 작은 것 저장