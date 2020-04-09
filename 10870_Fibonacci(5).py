from sys import stdin

fibo_list = [0, 1]

def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n - 1) + fibo(n - 2)

n = int(stdin.readline())
print(fibo(n))
