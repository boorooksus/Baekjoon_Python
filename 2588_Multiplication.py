a = input()
b = input()
a = int(a)
b = int(b)
x = b % 10
print(x * a)
x = (b // 10) % 10
print(x * a)
x = b // 100
print(x * a)
print(a * b)
