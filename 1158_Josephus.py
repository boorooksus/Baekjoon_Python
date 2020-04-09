from sys import stdin

n, k = map(int, stdin.readline().split())
s = [i + 1 for i in range(n)]
josep = []

idx = 0
while len(s) != 1:
    idx = (idx + k - 1) % len(s)
    josep.append(s[idx])
    del s[idx]


print("<", end='')
for i in range(n - 1):
    print(josep[i], end=', ')
print("%s>"%s[-1])

#문해기 3주차 문제 유형?