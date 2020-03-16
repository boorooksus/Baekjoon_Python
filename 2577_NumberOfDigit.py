a = int(input())
b = int(input())
c = int(input())
digit = [0] * 10
multi = str(a * b * c)

for i in range(len(multi)):
    index_ = int(multi[i])
    digit[index_] += 1
for i in range(10):
    print(digit[i])
