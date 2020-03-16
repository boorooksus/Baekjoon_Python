from sys import stdin

n = int(stdin.readline())
members = []
for i in range(n):
    members.append([i, stdin.readline().split()])
members.sort(key= lambda x: (int(x[1][0]), x[0]))
for i in range(n):
    print(members[i][1][0], members[i][1][1])
