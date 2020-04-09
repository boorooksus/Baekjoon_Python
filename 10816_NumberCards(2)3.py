from sys import stdin

n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
cards_dict = {}
for i in range(n):
    if cards[i] in cards_dict:
        cards_dict[cards[i]] += 1
    else:
        cards_dict[cards[i]] = 1
m = int(stdin.readline())
x_list = list(map(int, stdin.readline().split()))

for x in x_list:
    if x in cards_dict:
        print(cards_dict[x], end=' ')
    else:
        print(0, end=' ')

#dict 이용
#원래는 이분 탐색도 가능
