from sys import stdin

n = int(stdin.readline())
port = []
rightPort = list(map(int, stdin.readline().split()))
for i in range(n):
    if i + 1 > rightPort[i]:
        port.append([rightPort[i], i + 1])
    else:
        port.append([i + 1, rightPort[i]])

print(port)

port_sorted = sorted(port, key = lambda x : (x[1], x[0]))

print(port_sorted)
for i in range(1, len(port)):
    if port[i][0] == port[i - 1][0] and\
        port[i][1] == port[i - 1][1]:
        del port[i]
        i -= 1

cnt = 0
end = 0
for i in port_sorted:
    if i[0] >= end:
        print(i[0], i[1])
        cnt += 1
        end = i[1]
print(cnt)

