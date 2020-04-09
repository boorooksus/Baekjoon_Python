from sys import stdin
import heapq
INF = 100000001

def dijkstra(s):
    global n, m
    d_list = [INF for _ in range(n + 1)]
    d_list[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))
    while pq:
        dist, cur = heapq.heappop(pq)
        if dist > d_list[cur]:
            continue
        for nxt, nxt_dist in graph[cur]:
            nxt_dist += dist
            if nxt_dist < d_list[nxt]:
                d_list[nxt] = nxt_dist
                heapq.heappush(pq, (nxt_dist, nxt))
    return d_list


T = int(stdin.readline())
for i in range(T):
    #n, m, t:number of intersection, roads between intersection
    #possible destination
    n, m, t = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    #s:start point, g,h:intersection point
    s, g, h = map(int, stdin.readline().split())
    for j in range(m):
        #length of a to b : d
        a, b, d = map(int, stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    x_list = []
    for j in range(t):
        #possible destination(t)
        x = int(stdin.readline())
        x_list.append(x)
    #(s to g 와 h to x) or (s to h, g to x) 존재하는 목적지를 찾는다
    ans_list = []
    dFromS = dijkstra(s)
    dFromH = dijkstra(h)
    dFromG = dijkstra(g)
    # ==== 1 ==============================
    for j in x_list:
        if dFromS[j] == dFromS[h] + dFromH[g] + dFromG[j]\
            or dFromS[j] == dFromS[g] + dFromG[h] + dFromH[j]:
            ans_list.append(j)
    '''if dFromS[g] != INF:
        dFromH = dijkstra(h)
        for j in x_list:
            if j != INF:
                ans_list.append(j)
    if dFromS[h] != INF:
        dFromG = dijkstra(g)
        for j in x_list:
            if j != INF:
                ans_list.append(j)'''
    ans_list = list(set(ans_list))
    ans_list.sort()
    print(*ans_list)

#다익스트라
# 1: 단순히 도착 g, h를 거쳐서 후보 도착지까지 갈 수 있는지 묻는게 아님!
        #출발지점에서 후보도착지 까지 최소 거리 ==
            #출발지점에서 g, h지점 거친 후 후보 도착지 까지 거리
    #를 만족 하는 후보 도착지를 찾는 문제