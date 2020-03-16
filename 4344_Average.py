c = int(input())
for i in range(c):
    point = list(map(int, input().split()))
    average = (sum(point) - point[0]) / point[0]
    count = 0
    for j in range(1, point[0] + 1):
        if point[j] > average:
            count += 1
    print("%.3f%%" %round((count / point[0]) * 100, 3))
