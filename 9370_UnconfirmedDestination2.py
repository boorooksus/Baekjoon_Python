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

    ans_list = []
    '''for nxt, nxtDist in graph[s]:
        if nxt == g:
            for hnxt, hnxtDist in graph[h]:
                if hnxt in x_list:
                    ans_list.append(hnxt)
        if nxt == h:
            for gnxt, gnxtDist in graph[g]:
                if gnxt in x_list:
                    ans_list.append(gnxt)'''

    ans_list = sorted(list(set(ans_list)))
    print(*ans_list)
