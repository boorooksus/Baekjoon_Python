from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

parent = [i for i in range(n + 1)]
def getParent(x):
    if x == parent[x]: return x
    parent[x] = getParent(parent[x])
    return parent[x]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a > b: parent[a] = b
    else: parent[b] = a
    return



arr = [[0] for i in range(n + 1)]

for i in range(1, n + 1):
    col_str = stdin.readline()
    col_list = col_str.split(' ')
    for j in col_list:
        arr[i].append(int(j))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            unionParent(i, j)

city_str = stdin.readline()
city_list = city_str.split(' ')
cityParent = []
for i in city_list:
    cityParent.append(getParent(int(i)))
cityParent = set(cityParent)
if len(cityParent) > 1: print("NO")
else: print("YES")



