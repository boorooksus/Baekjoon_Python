from sys import stdin

s = []

def push(cmd):
    idx = cmd.index(' ') + 1
    x = int(cmd[idx:-1])
    s.append(x)

def pop():
    if len(s) == 0:
        print(-1)
    else:
        print(s[-1])
        s.pop()

def size():
    print(len(s))

def empty():
    if len(s) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(s) == 0:
        print(-1)
    else:
        print(s[-1])

n = int(stdin.readline())
for i in range(n):
    cmd = stdin.readline()
    if cmd[:4] == "push":
        push(cmd)
    elif cmd[:3] == "pop":
        pop()
    elif cmd[:4] == "size":
        size()
    elif cmd[:5] == "empty":
        empty()
    else:
        top()

#스택
#cmd.split()[0] 이런식으로 쪼갤수 있다다