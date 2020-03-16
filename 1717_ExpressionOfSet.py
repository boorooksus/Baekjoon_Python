from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

n, m = map(int, stdin.readline().split())

parent = []
def getParent(x):
    if parent[x] == x:
        return x
    #else: return parent[x]
    parent[x] = getParent(parent[x])
    return parent[x]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a > b: parent[a] = b
    else: parent[b] = a
    return

def isSameParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a == b:
        print("YES")
    else:
        print("NO")

    return

for i in range(n + 1):
    parent.append(i)

for i in range(m):
    operator, a, b = map(int, stdin.readline().split())
    if operator == 0:
        unionParent(a, b)
    elif operator == 1:
        isSameParent(a, b)
