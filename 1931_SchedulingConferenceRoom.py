from sys import stdin

n = int(stdin.readline())
conference = [] #각 회의의 시작과 끝이 저장된 리스트를 저장하는 리스트
#회의의 시작과 끝을 리스트로 저장하고 conference 리스트에 넣는다
# time =[start, end]
for i in range(n):
    time = list(map(int, stdin.readline().split()))
    conference.append(time)

# == 1 ==
#회의 끝을 key값으로 하는 오름차순으로 정렬
#끝시간이 같다면 시작 시간을 key 값으로 오름차순으로 정렬
conference_sorted = sorted(conference, key = lambda x: (x[1], x[0]))

cnt = 0
end = 0
for i in conference_sorted:
    if i[0] >= end:
        cnt += 1
        end = i[1]

print(cnt)

#그리디 알고리즘
#문해기 2주차 보강 Game 문제 유형
# 1 : lambda 사용법 기억하기(lamda가 아니라 lambda이다)
    #다중 조건으로 sort하는 방법 기억하기
    #끝이 같을 때 시작 기준 오름차순 안하게 되면
    #[8 , 8], [8, 8], [3, 8], [8 , 8]
    #여기서 답이 4가 아니라 3이라고 나옴
