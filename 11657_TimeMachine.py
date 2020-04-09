from sys import stdin
from collections import deque
INF = 500000001

def ballmanFord(start):
    global n, m
    d[start] = 0
    cycle = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for nxt, nxt_dist in line[j]:
                nxt_dist += d[j]
                # === 1 =================================
                if d[j] != INF and nxt_dist < d[nxt]:
                    d[nxt] = nxt_dist
                    if i == n:
                        cycle = 1

    #사이클이 있다면 무한히 오래전으로 되돌릴 수 있음
    if cycle == 1:
        print(-1)
        return

    for i in range(1, n + 1):
        if i == start:
            continue
        #경로가 존재하지 않을 때
        if d[i] == INF:
            print(-1)
        else:
            print(d[i])

#n : number of cities, m : number of bus line
n, m = map(int, stdin.readline().split())
line = [[]for _ in range(n + 1)]
for _ in range(m):
    #take c from a to b
    a, b, c = map(int, stdin.readline().split())
    line[a].append((b, c))
d = [INF for _ in range(n + 1)]
ballmanFord(1)

#벨만 포드 알고리즘
# 1 : 조건문에서 d[j] != INF 꼭 체크해야함
    #안하면 길이 없어서 INF 상태인데 음의 길이가 더해져서
    #데이터 추가 될 수 있음
#코드 참고 : https://deliorange.tistory.com/88
