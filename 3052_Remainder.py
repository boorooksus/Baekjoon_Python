num = []
count_ = 0
for i in range(10):
    x = int(input())
    x %= 42
    if num.count(x) == 0:
        count_ += 1
    num.append(x)
print(count_)
