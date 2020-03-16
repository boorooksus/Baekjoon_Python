t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    result = ''
    for i in s:
        result += i * r
    print(result)