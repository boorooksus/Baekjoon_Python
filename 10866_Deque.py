from sys import stdin


n = int(stdin.readline())
deque = []
for _ in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == 'push_back':
        deque.append(int(cmd[1]))
    elif cmd[0] == 'push_front':
        temp = [int(cmd[1])]
        deque = temp + deque
    elif cmd[0] == 'pop_front':
        if deque:
            print(deque[0])
            del deque[0]
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if deque:
            print(deque[-1])
            del deque[-1]
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)

