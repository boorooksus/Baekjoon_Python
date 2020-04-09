from sys import stdin
MAX = 1000000000
n, s = map(int, stdin.readline().split())
sequence = list(map(int, stdin.readline().split()))

ans = MAX
start = 0
end = 0
sum = sequence[0]

while(end < n - 1):
    end += 1
    sum += sequence[end]
    #부분합 조건 만족하는 경우
    while(sum >= s):
        len = end - start + 1
        if len < ans:
            ans = len
        #startPoint를 뒤로 이동시킨다.
        sum -= sequence[start] 
        start += 1 #==1==

#==2==합 만드는 것이 불가능 할 때 0으로 바꾸기
if ans == MAX:
    ans = 0

print(ans)


#문해기 2주차 보강 String 문제 참조
#startPoint와 endPoint 둬서 수열 탐색
#==1== +안하고 -했다가 답 이상하게 나옴
#==2== 이거 안했다가 틀림