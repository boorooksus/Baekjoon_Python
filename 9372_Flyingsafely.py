from sys import stdin


def get_parent(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]


def union_parent(x, y):
    x = get_parent(x)
    y = get_parent(y)
    if parent[x] < parent[y]:
        parent[y] = x
        tree_size[x] += tree_size[y]
    else:
        parent[x] = y
        tree_size[y] += tree_size[x]


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    path = [[0] for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]
    tree_size = [0 for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        path[a].append(b)
        path[b].append(a)

    ans = 0
    for i in range(1, n + 1):
        for j in range(1, len(path[i])):
            if get_parent(path[i][j]) != get_parent(i):
                union_parent(i, path[i][j])
                ans += 1

    print(ans)


# MST, BFS 두 가지 방법으로 풀어도 됨
# 더 쉬운 방법은 n-1 출력
# (모든 국가가 연결되어 있으므로 mst 크기는 n-1)
