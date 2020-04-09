from sys import stdin
import heapq

INF = 810001
n, e = map(int, stdin.readline().split())
graph = [[]for i in range(n + 1)]


for i in range(e):
    a, b, c = map(int, stdin.readline().split())
    # === 1 ==================
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, stdin.readline().split())

def dijkstra(start, end):
    d = [INF for i in range(n + 1)]
    pq = []

    d[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        dist, cur = heapq.heappop(pq)

        if dist > d[cur]:
            continue
        for next, next_dist in graph[cur]:
            next_dist += dist
            if next_dist < d[next]:
                d[next] = next_dist
                heapq.heappush(pq, (next_dist, next))

    return d[end]


one2v1 = dijkstra(1, v1)
v1tov2 = dijkstra(v1, v2)
v1toN = dijkstra(v1, n)
v2toN = dijkstra(v2, n)
one2v2 = dijkstra(1, v2)

path1 = one2v1 + v1tov2 + v2toN
path2 = one2v2 + v1tov2 + v1toN

#path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
#path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)


if path1 >= INF and path2 >= INF:
    print(-1)
elif path1 < path2:
    print(path1)
elif path2 <= path1:
    print(path2)


#다익스트라
# 1 : 양방향 그래프이기 때문에 a, b 각각 저장해준다