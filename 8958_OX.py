n = int(input())
for i in range(n):
    ox = str(input())
    point = 0
    total = 0
    for j in range(len(ox)):
        if ox[j] == 'O':
            point += 1
            total += point
        else:
            point = 0
    print(total)