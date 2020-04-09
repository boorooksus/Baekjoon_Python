from sys import stdin

def binary(lis, key):
    low = 1
    high = len(lis)
    while(high >= low):
        mid = (low + high) // 2

        if key < lis[mid]:
            high = mid - 1
        elif key == lis[mid]:
            return mid
        else:
            low = mid + 1
    return low


n = int(stdin.readline())
rightPort = list(map(int, stdin.readline().split()))

ans = 0
lis = [0]
for i in range(n):
    if rightPort[i] > lis[-1]:
        lis.append(rightPort[i])
        ans += 1
    else:
        idx = binary(lis, rightPort[i])
        lis[idx] = rightPort[i]
print(ans)


#이진탐색
#최장 증가 수열 알고리즘(LIS)
#C++에서는 lower_bound 사용하면 됨
#문해기 2주차 보강 Game 유형
