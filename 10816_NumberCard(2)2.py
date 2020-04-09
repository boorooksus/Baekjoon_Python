from sys import stdin

n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
cards.sort()
m = int(stdin.readline())
x_list = list(map(int, stdin.readline().split()))

for x in x_list:
    cnt = 0
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if x < cards[mid]:
            right = mid
        elif x == cards[mid]:
            cnt += 1
            idx = 1
            while mid - idx >= 0 and cards[mid - idx] == x:
                cnt += 1
                idx += 1
            idx = 1
            while mid + idx < n and cards[mid + idx] == x:
                cnt += 1
                idx += 1
            break
        else:
            left = mid + 1

    print(cnt, end=' ')