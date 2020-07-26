from sys import stdin

def asce(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) < 10:
            num.pop()


min, max = map(str, stdin.readline().split())

ans = 0
if min == 1:
    ans += 1

