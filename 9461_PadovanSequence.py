from sys import stdin

padovan_list = [-1, 1, 1, 1, 2, 2]
#padovan_list.append(-1 for i in range(5, 101))
for i in range(5, 101):
    padovan_list.append(-1)
def padovan(n):
    if padovan_list[n] != -1: return padovan_list[n]
    result = padovan(n - 1) + padovan(n - 5)
    padovan_list[n] = result
    return result

t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    print(padovan(n))
