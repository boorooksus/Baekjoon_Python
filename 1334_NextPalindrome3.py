from sys import stdin
from collections import deque
MAX = 10 ** 25
def palindrome(x):
    x_list = list(int(i) for i in str(x))
    #x_list = list(map(int, list(str(x))))
    #x_list = deque()
    #x_list.append(int(i) for i in str(x))
    l = len(x_list)
    while(1):
        isChanged = False
        for i in range(l // 2):
            fidx = i
            bidx = l - i - 1
            if x_list[bidx] > 9:
                x_list[bidx - 1] += x_list[bidx] // 10
                x_list[bidx] %= 10
            if x_list[fidx] > 9:
                if fidx == 0:
                    x_list.insert(0, x_list[fidx] // 10)
                    x_list[fidx] %= 10
                else:
                    x_list[fidx - 1] += x_list[fidx] // 10
                    x_list[fidx] %= 10

            if x_list[fidx] == x_list[bidx]:
                continue
            elif x_list[fidx] < x_list[bidx]:
                isChanged = True
                x_list[bidx - 1] += 1
                x_list[bidx] = x_list[fidx]
            else:
                isChanged = True
                x_list[bidx] = x_list[fidx]

        if isChanged == False:
            ans = 0
            for i in range(l):
                ans = ans * 10 + x_list[i]
            print(ans)
            return



                #123456 123451 123521 124421
                #12344334 12344341 12344421 12345321 12355321
                #12347891 12347921 12348321 12355321
                #12348991 12349021 12349321 12355321
                #1234331 1234421 1235321


n = int(stdin.readline())
palindrome(n)