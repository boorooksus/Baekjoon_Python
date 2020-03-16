num = list()
max_ = 0
index_ = 0
for i in range(9):
    num.append(input())
print(max(num), num.index(max(num)) + 1)