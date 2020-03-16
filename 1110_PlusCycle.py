n = int(input())
cycle = 0
x = n
while True:
    x = (x % 10) * 10 + ((x // 10) + (x % 10)) % 10
    cycle += 1
    if n == x:
        break
print(cycle)