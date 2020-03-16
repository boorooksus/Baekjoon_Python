from sys import stdin

n = int(stdin.readline())
fibo_list = [-1] * (n + 1)
fibo_list[0] = 0
fibo_list[1] = 1

def fibonacci(x):
    if fibo_list[x] != -1: return fibo_list[x]
    ans = fibonacci(x-1) + fibonacci(x-2)
    fibo_list[x] = ans
    return ans

print(fibonacci(n))