n = int(input())
a = -1
b = -1
for i in range(n // 5, -1, -1):
    if (n - (i * 5)) % 3 == 0:
        a = i
        b = (n - 5 * a) // 3
        break
    else:
        continue
print(-1 if a == -1 or b == -1 else a + b)

#5a + 3b = n
#a = n // 5
# 나머지 : a % 5
# b = 나머지 // 3 ( b % 3 == 0)