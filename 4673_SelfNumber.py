def d(a):
    result = a
    while a != 0:
        result += a % 10
        a = a // 10
    return result

def selfNumber():
    a = [0] * 10001
    i = 1
    while d(i) <= 10000:
        a[int(d(i))] = 1
        i += 1
    return a

a = selfNumber()
for i in range(1, 10001):
    if(a[i] == 0):
        print(i)

