from sys import stdin
import heapq

INF = 1000001

def dijkstra(n, m, k):
    d_list = [[INF for _ in range(10002)] for _ in range(102)]
    for i in range(10001):
        d_list[1][i] = 0
    pq = []
    heapq.heappush(pq, (0, 0, 1)) #distance, cost, next

    while pq:
        #d : distance, c : cost, v : vertex
        curD, curC, curV = heapq.heappop(pq)
        if curD > d_list[curV][curC]:
            continue
        for nextD, nextC, nextV in flight[curV]:
            nextD += d_list[curV][curC]
            nextC += curC
            if nextC > m:
                continue
            if nextD < d_list[nextV][nextC]:
                # ==== 1 ======================================
                for i in range(nextC, m + 1):
                    if d_list[nextV][i] > nextD:
                        d_list[nextV][i] = nextD
                heapq.heappush(pq, (nextD, nextC, nextV))
    ans = min(d_list[n])
    if ans == INF:
        print("Poor KCM")
    else:
        print(ans)

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

#파이썬으로 다익스트라 + DP 쓰면 시간초과
# 1 : 이해 안됨