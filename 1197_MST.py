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
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


edge = []
v, e = map(int, stdin.readline().split())
parent = [i for i in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    edge.append((c, a, b))

edge.sort()
ans = 0
for i in edge:
    c, a, b = i
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        ans += c

print(ans)


# MST
