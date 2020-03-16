from sys import stdin

t = int(stdin.readline())

def zero_cnt(x, zero_list):
    if zero_list[x] != -1: return zero_list[x]
    ans = zero_cnt(x-1, zero_list) + zero_cnt(x-2, zero_list)
    zero_list[x] = ans
    return ans

def one_cnt(x, one_list):
    if one_list[x] != -1: return one_list[x]
    ans = one_cnt(x-1, one_list) + one_cnt(x-2, one_list)
    one_list[x] = ans
    return ans

for i in range(t):
    n = int(stdin.readline())
    zero_list = [-1] * 41
    zero_list[0] = 1
    zero_list[1] = 0
    one_list = [-1] * 41
    one_list[0] = 0
    one_list[1] = 1
    print(zero_cnt(n, zero_list), one_cnt(n, one_list))


