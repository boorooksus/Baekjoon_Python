from sys import stdin

rgb_list = []
cost_list = []
n = int(stdin.readline())
check = [False, False, False]
check_list = [check] * (n + 1)

for i in range(n):
    r, g, b = map(int, stdin.readline().split())
    rgb = [r, g, b]
    rgb_list.append(rgb)

def getCost(cnt, cost):
    if cnt == n:
        cost_list.append(cost)
        return

    for i in range(3):
        if check_list[cnt][i] == True:
            continue
        #check_list[cnt][i] = True
        check_list[cnt + 1][i] = True
        getCost(cnt + 1, cost + rgb_list[cnt][i])
        check_list[cnt + 1][i] = False

getCost(0, 0)
cost_list.sort()
print(cost_list[0])

