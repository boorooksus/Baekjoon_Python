from sys import stdin

n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
cards.sort()
m = int(stdin.readline())
x_list = list(map(int, stdin.readline().split()))

for x in x_list:
    copy = cards[:]
    cnt = 0
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if x < copy[mid]:
            right = mid
        elif x == copy[mid]:
            cnt += 1
            idx = 1
            while mid - idx > -1 and copy[mid - idx] == x
                if copy[mid - idx] == x:
                    cnt += 1
            while mid + idx < n and copy[mid + idx] == x:
                if copy[mid + idx] == x:
                    cnt += 1
                idx += 1
            break

        elif x > copy[mid]:
            left = mid + 1
    print(cnt, end=' ')