from sys import stdin
from collections import deque

q = deque()
n = int(stdin.readline())
for i in range(1, n + 1):
    q.appendleft(i)
while(len(q) > 1):
    q.pop()
    temp = q.pop()
    q.appendleft(temp)

print(q.pop())
