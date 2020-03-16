import sys
from collections import Counter

n = int(sys.stdin.readline())
ints = [int(sys.stdin.readline()) for i in range(n)]

#arith : 산술평균
print(round(sum(ints) / n))
#mid : 중앙값
ints.sort()
print(ints[n // 2])
#mode = 최빈값
if n == 1:
    print(ints[0])
else:
    modes_list = Counter(ints).most_common()
    if modes_list[0][1] == modes_list[1][1]:
        for i in range(len(modes_list)):
            if modes_list[0][1] != modes_list[i][1]:
                modes_list[i] = (4000,0)
        modes_list.sort(key=lambda x: x[0])
        print(modes_list[1][0])
    else:
        print(modes_list[0][0])
#scope : 범위
print(ints[-1] - ints[0])
