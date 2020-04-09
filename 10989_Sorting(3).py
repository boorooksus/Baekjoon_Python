from sys import stdin
MAX = 10001

originalList = []
cnt_list = [0 for i in range(MAX)]
cntsum_list = [0 for i in range(MAX)]

n = int(stdin.readline())

sortedList = [0 for i in range(n)]

for i in range(n):
    x = int(stdin.readline())
    originalList.append(x)
    cnt_list[x] += 1

cntsum_list[0] = cnt_list[0]
for i in range(1, MAX):
    cntsum_list[i] = cntsum_list[i - 1] + cnt_list[i]

for i in range(n - 1, -1, -1):
    # == 1 ==
    sortedList[cntsum_list[originalList[i]] - 1] = originalList[i]
    cntsum_list[originalList[i]] -= 1

for i in range(n):
    print(sortedList[i])
    

#Counting Sort 일반적인 방법
#시간초과 발생(다음 버전 참고)
# 1 : cntsum_list[originalList[i]] 다음에 -1 꼭 해줘야함