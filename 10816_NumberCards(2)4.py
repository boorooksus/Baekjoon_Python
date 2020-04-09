from sys import stdin

n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
cards.sort()
m = int(stdin.readline())
x_list = list(map(int, stdin.readline().split()))

for x in x_list:
    loweridx = 0
    upperidx = 0
    cnt = 0
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if x <= cards[mid]:
            if x > cards[mid - 1]:
                loweridx = mid
            right = mid
        elif x >= cards[mid]:
            if x < cards[mid + 1]:
                upperidx = mid + 1
            left = mid + 1


    print(loweridx - upperidx, end=' ')