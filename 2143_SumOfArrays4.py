from sys import stdin

t = int(stdin.readline())
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))
#== 1 ==
aSum = {}
bSum = {}

#aSum에 a배열 부분합의 모든 경우 딕셔너리로 저장
for start in range(n):
    sum = 0
    for end in range(start, n):
        sum += a[end]
        #딕셔너리에 이미 키 존재하면 카운트 추가
        if aSum.get(sum):
            aSum[sum] += 1
        #딕셔너리에 키가 존재하지 않으면 추가해야함
        else:
            aSum[sum] = 1

for start in range(m):
    sum = 0
    for end in range(start, m):
        sum += b[end]
        if bSum.get(sum):
            bSum[sum] += 1
        else:
            bSum[sum] = 1


cnt = 0

#== 1 ==
'''for x in aSum:
    for y in bSum:
        if x + y == t:
            cnt += aSum[x] * bSum[y]'''

#== 2 ==
for ai, ak in enumerate(aSum):
    if bSum.get(t - ak):
        cnt += aSum[ak] * bSum[t - ak]

print(cnt)

#최종 성공
#이중 포인터 사용
#1 : 딕셔너리 안하고 리스트로 했다가 시간초과
#2 : 딕셔너리에서 enumerate는 인덱스와 키 값을 튜플로 반환
    #(키값과 value 값을 튜플로 반환하는 것이 아니다)
