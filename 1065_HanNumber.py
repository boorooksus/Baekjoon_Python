def isHansoo(n):
    if n // 10 == 0:
        return 1
    digit = str(n)
    gap = int(digit[1]) - int(digit[0])
    result = 1
    for i in range(1, len(digit)):
        if gap != int(digit[i]) - int(digit[i - 1]):
            result = 0
            break
    return result

x = int(input())
cnt = 0
for i in range(1, x + 1):
    if(isHansoo(i) == 1):
        cnt += 1
print(cnt)