from sys import stdin

def cntLAN(length):
    global k
    cnt = 0
    for i in lan:
        cnt += i // length
    return cnt

def binarySearch():
    global n
    global k

    #==== 1 ==========================
    left = 1
    right = lan[-1]
    #==== 2 =============================
    if cntLAN(right) >= n:
        return right
    else:
        max = 0
        
    while left < right:
        mid = (left + right) // 2
        cnt = cntLAN(mid)
        if cnt < n:
            right = mid
        elif cnt >= n:
            if max < mid:
                max = mid
            left = mid + 1
    return max


k, n = map(int, stdin.readline().split())
lan = []
for i in range(k):
    lan.append(int(stdin.readline()))
lan.sort()
print(binarySearch())


#이분탐색
#1 : 처음에 left를 0으로 초기화 했다가 런타임 에러남
    #(mid가 0이 돼어 0으로 나누는 경우가 있을 수 있음)
#2 : 이렇게 안하면 right이 답일때 while문에서 right까지 못가고 끝남
