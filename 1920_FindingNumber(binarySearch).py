from sys import stdin

n = int(stdin.readline()) #a 원소의 개수
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline()) #x 원소의 개수
x_list = list(map(int, stdin.readline().split())) #찾아야하는 수

a.sort()

for x in x_list:

    left = 0
    right = n
    mid = 0
    isDone = False
    while left < right:
        mid = (left + right) // 2
        if x < a[mid]:
            right = mid
        elif x == a[mid]:
            print(1)
            isDone = True
            break
        elif x > a[mid]:
            # === 1 ==================
            left = mid + 1

    if isDone == False:
        print(0)


#이진 탐색
#1 : mid + 1 안하면 while문 못 빠져나간다