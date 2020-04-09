from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(stdin.readline())
h = list(map(int, stdin.readline().split()))
h_dict = {}
cnt = 0


for i in range(n):
    if (h[i] + 1) not in h_dict or h_dict[h[i] + 1] == 0:
        if h[i] in h_dict:
            h_dict[h[i]] += 1
        else:
            h_dict[h[i]] = 1
        cnt += 1
    else:
        h_dict[h[i] + 1] -= 1
        if h[i] in h_dict:
            h_dict[h[i]] += 1
        else:
            h_dict[h[i]] = 1

print(cnt)

#문해기 3주차 유형
#높이 h[i]인 풍선을 입력 받았을 때,
   #h[i] + 1인 높이에서 날아오는 화살이 있는지 검사사