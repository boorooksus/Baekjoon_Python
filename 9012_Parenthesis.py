from sys import stdin


def vps():
    s = []
    ps = list(stdin.readline().strip())
    for i in ps:
        if i == '(':
            s.append(i)
        elif len(s) == 0:
            print("NO")
            return
        else:
            s.pop()
    if len(s) == 0:
        print("YES")
    else:
        print("NO")
    return


t = int(stdin.readline())
for _ in range(t):
    vps()
