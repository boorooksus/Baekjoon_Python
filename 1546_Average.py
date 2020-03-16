n = int(input())
score = list(map(int, input().split()))
max_ = max(score)
for i in range(n):
    score[i] = round((score[i] / max_) * 100, 3)
average = sum(score) / n
print(average)