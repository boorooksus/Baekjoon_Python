from sys import stdin
from collections import deque

s = stdin.readline()
sl = len(s)

for i in range((sl // 2 - 1) * 10 + 5, (len(s) - 1) * 10, 5):
    front = i // 10
    rear = i // 10 + 1


if len(s) % 2 == 1:
    for i in range((sl // 2) * 10, (len(s) - 1) * 10, 5):

def palindrome(s):
    if len(s) == 1:
        print(1)
        return

    sl = len(s)
    #s = [s[0]]
    s = [i for i in s[:sl // 2]]
    for i in range(sl // 2, sl - 1):
        cur = s[i]
        next = s[i + 1]
        




palindrome(s)