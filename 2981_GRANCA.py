from sys import stdin
from math import gcd

n = int(stdin.readline())
num = []
m = []
for i in range(n):
    num.append(int(stdin.readline()))

while(1 not in num):
    res = num[0]
    for i in num[1:]:
        res = gcd(res, i)
    if res not in m and res != 1:
        m.append(res)
    for i in range(len(num)):
        num[i] -= 1

print(*m)
