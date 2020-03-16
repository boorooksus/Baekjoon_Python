from sys import stdin

n = int(stdin.readline())
cdn = []
for i in range(n):
    cdn.append(list(map(int, stdin.readline().split())))
cdn.sort()
for i in range(n):
    print(cdn[i][0], cdn[i][1])

