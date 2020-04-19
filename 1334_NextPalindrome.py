from sys import stdin
MAX = 10 ** 50
def isPalindrome(x):
    num_str = str(x)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[len(num_str) - i - 1]:
            return False
    return True


n = int(stdin.readline())
while(n < MAX):
    n += 1
    if isPalindrome(n):
        print(n)
        break