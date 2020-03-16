from sys import stdin
from math import factorial

fact_list = [-1] * 1000001
fact_list[0] = 1
def dinamicFact(x):
    if fact_list[x] != -1: return fact_list[x]
    result = factorial(x)
    fact_list[x] = result
    return result

def moreDinamicFact(x):
    if fact_list[x] != -1: return fact_list[x]
    result = x * moreDinamicFact(x-1)
    fact_list[x] = result
    return result

def comb(n, r):
    result = 1
    for i in range(r):
        result *= n - i
        result //= r - i
    return result

n = int(stdin.readline())

cnt = 0
for i in range(0, (n // 2) + 1):
    #cnt += dinamicFact(n - i) // (dinamicFact(n - 2 * i) * dinamicFact(i))
    #cnt += comb(n - i, i)
    cnt += moreDinamicFact(n - i) // (moreDinamicFact(n - 2 * i) * moreDinamicFact(i))

print(cnt % 15746)