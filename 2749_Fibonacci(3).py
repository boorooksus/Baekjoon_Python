from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

mod = 1000000
n = int(stdin.readline())

def multi(x, y):
    if y == 1:
        for i in range(2):
            for j in range(2):
                x[i][j] %= mod
        return x
    res = [[0, 0], [0, 0]]
    if y % 2 == 1:
        temp = multi(x, y - 1)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    res[i][j] = (res[i][j] + (x[i][k] * temp[k][j]) % mod) % mod

    else:
        temp = multi(x, y // 2)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    res[i][j] = (res[i][j] + (temp[i][k] * temp[k][j]) % mod) % mod
    return res

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    x = [[1, 1], [1, 0]]
    res = multi(x, n - 1)
    print(res[0][0])

#분할 정복
#행렬 곱셈을 응용해 피보나치 수를 구하는 문제
#피사노 주기 이용한 풀이도도 가능