from sys import stdin
MAX = 10001

cnt_list = [0 for i in range(MAX)]
n = int(stdin.readline())

for i in range(n):
    x = int(stdin.readline())
    cnt_list[x] += 1


for i in range(MAX):
    for j in range(cnt_list[i]):
        print(i)

#Counting Sort
#원본배열 저장하고 중복 합 배열 구하고 원본 배열 거꾸로 가면서 정렬 배열에 저장하면
    #메모리 초과 발생
#위의 처럼 카운트 배열에 값이 0이 아니면 해당 숫자만큼 출력하도록 바꿈
#(이전 버전 참고)
#radix sort(기수정렬) 사용하면 메모리 초과(모든 입력을 배열에 저장해야해서)