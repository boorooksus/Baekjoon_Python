from sys import stdin

n = int(stdin.readline())
sq = list(map(int, stdin.readline().split()))
op = list(map(int, stdin.readline().split()))
infix = [sq[0]]
used = op[:]
min_res = 10 ** 9
max_res = -10 ** 9


def dfs(operator, cur, n):
    global min_res, max_res
    if used[operator] == 0:
        return

    if cur == n - 2:
        infix.append(operator)
        infix.append(sq[cur + 1])
        res = infix[0]
        for i in range(1, 2 * n - 1, 2):
            if infix[i] == 0:
                res += infix[i + 1]
            elif infix[i] == 1:
                res -= infix[i + 1]
            elif infix[i] == 2:
                res *= infix[i + 1]
            elif infix[i] == 3:
                if res >= 0:
                    res //= infix[i + 1]
                else:
                    res =(-res // infix[i + 1]) * -1

        if min_res > res:
            min_res = res
        if max_res < res:
            max_res = res
        del infix[-1]
        del infix[-1]
        return

    used[operator] -= 1
    infix.append(operator)
    infix.append(sq[cur + 1])
    for i in range(4):
        dfs(i, cur + 1, n)
    used[operator] += 1
    del infix[-1]
    del infix[-1]
    return



for i in range(4):
    dfs(i, 0, n)

print(max_res)
print(min_res)






