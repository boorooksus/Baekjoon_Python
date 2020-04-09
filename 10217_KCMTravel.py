from sys import stdin
import heapq

INF = 1000001

def dijkstra(n, m, k):
    d_list = [INF for _ in range(n + 1)]
    d_list[1] = 0
    pq = []
    heapq.heappush(pq, (0, 0, 1))

    while pq:
        #d : distance, c : cost, v : destination
        curD, curC, curV = heapq.heappop(pq)
        if curD > d_list[curV]: continue
        for nextD, nextC, nextV in flight[curV]:
            nextD += d_list[curV]
            nextC += curC
            if nextD < d_list[nextV] and nextC <= m:
                d_list[nextV] = nextD
                heapq.heappush(pq, (nextD, nextC, nextV))

    if d_list[n] == INF:
        print("Poor KCM")
    else:
        print(d_list[n])
    return


T = int(stdin.readline())
for _ in range(T):
    #n : number of airport
    #m : maximum cost
    #k : number of ticket
    n, m, k = map(int, stdin.readline().split())
    flight = [[]for _ in range(n + 1)]
    for i in range(k):
        #u : departure, v : destination
        #c : cost, d : distance
        u, v, c, d = map(int, stdin.readline().split())
        flight[u].append((d, c, v))
    dijkstra(n, m, k)
