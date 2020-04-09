from sys import stdin
import heapq

INF = 300001
#v : 정점의 개수, e : 간선의 갯수
v, e = map(int, stdin.readline().split())
a = [[[0, 0]] for i in range(v + 1)] #간선 관계 저장
d = [INF for j in range(v + 1)] #최소 거리 저장
#k : start point
k = int(stdin.readline())
#u -> v : w
for i in range(e):
    x, y, z = map(int, stdin.readline().split())
    a[x].append([y, z])

def dijkstra(start):
    d[start] = 0
    pq = []
    heapq.heappush(pq, [start, 0])
    while(len(pq) != 0):
        cur_list = heapq.heappop(pq)
        cur_idx = cur_list[0]
        cur_dis = cur_list[1]

        if cur_dis > d[cur_idx]:
            continue
        for i in range(1, len(a[cur_idx])):
            next_idx = a[cur_idx][i][0]
            next_dis = a[cur_idx][i][1] + cur_dis

            if next_dis < d[next_idx]:
                d[next_idx] = next_dis
                heapq.heappush(pq, [next_idx, next_dis])

dijkstra(k)
for i in range(1, v + 1):
    if d[i] == INF:
        print("INF")
        continue
    print(d[i])


