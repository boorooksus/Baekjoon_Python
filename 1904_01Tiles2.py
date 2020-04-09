from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

#arr = [0, 1, 2, 3, 5]
def tile(x):
    if x == 1:
        return 1
    if x == 2:
        return 2

    a = 1
    b = 2
    temp = 0
    for i in range(x - 2):
        temp = (a + b) % 15746
        a = b
        b = temp

    return temp

n = int(stdin.readline())
print(tile(n))


#재귀로 풀 경우 메모리 초과