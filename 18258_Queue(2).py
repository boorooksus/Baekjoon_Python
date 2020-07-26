from sys import stdin
from collections import deque

q = deque()
n = int(stdin.readline())

for _ in range(n):
    cmd = stdin.readline().strip()

    if cmd[0:4] == "push":
        num = 0
        for i in cmd[5:]:
            num = num * 10 + int(i)
        q.appendleft(num)
    elif cmd == "pop":
        if not q:
            print(-1)
        else:
            print(q[-1])
            q.pop()
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif cmd == "back":
        if not q:
            print(-1)
        else:
            print(q[0])

#pypy로 채점해야 통과