from sys import stdin
s = stdin.readline()

n = list(map(int, s.strip()))

if 0 not in n:
    print(-1)
else:
    n.remove(0)
    if sum(n) % 3 != 0:
        print(-1)
    else:
        n.sort(reverse=True)
        ans = 0
        for i in n:
            ans = ans * 10 + i
        print(ans * 10)


#문해기 6주차 1번
#배수 판정법
