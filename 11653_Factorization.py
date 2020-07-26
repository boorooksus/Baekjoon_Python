from sys import stdin
import math

prime = [False for _ in range(10000001)]

def isPrime(x):
    if prime[x] == True:
        return True
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, round(math.sqrt(x)), 2):
        if x % i == 0:
            return False
    prime[x] = True
    return True

def solution(n):
    if isPrime(n):
        print(n)
        return
    factor = 2

    #이렇게 하면 시간초과과
   '''while(n > 1):
        if isPrime(factor) and n % factor == 0:
            print(factor)
            n /= factor
        else:
            factor += 1'''

    while factor <= round(math.sqrt(n)):
        if isPrime(factor) and n % factor == 0:
            print(factor)
            n //= factor
        else:
            factor += 1
    if n != 1:
        print(n)



n = int(stdin.readline())
solution(n)