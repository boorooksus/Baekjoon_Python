from sys import stdin

n = int(stdin.readline())
movie_array = [0]
cur = 666
while(len(movie_array) < n + 1):
    #== 1 ==
    cur_list = list(int(i) for i in str(cur))
    for i in range(len(cur_list) - 2):
        if cur_list[i] == 6 and cur_list[i + 1] == 6\
                and cur_list[i + 2] == 6:
            movie_array.append(cur)
            #== 2 ==
            break
    cur += 1

print(movie_array[n])

#브루트 포스 알고리즘
#2 : break 안하면 16660666이나 16666 처럼 중복/4개 이상 연속 숫자를 중복해서 넣음
#1 : 문자열을 리스트로 변환