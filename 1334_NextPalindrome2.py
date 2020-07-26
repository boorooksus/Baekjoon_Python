from sys import stdin
MAX = 10 ** 50
def palindrome(x):
    num_list = list(int(i) for i in str(x))
    l = len(num_list)
    if l % 2 == 1:
        for i in range(l // 2):
            front = num_list[i]
            back = num_list[l - i - 1]
            if back > front:
                num_list[l - i - 2] += 1
            num_list[l - i - 1] = front
    else:
        for i in range(l // 2 - 1):
            front = num_list[i]
            back = num_list[l - i - 1]
            if back > front:
                num_list[l - i - 2] += 1
            num_list[l - i - 1] = front
        mid = l // 2 - 1
        front = num_list[mid]
        back = num_list[l - mid - 1]
        if back > front:
            num_list[l - mid - 1] += 1
            num_list[mid] = num_list[l - mid - 1]

    for i in range(l):
        print(num_list[i], end='')



n = int(stdin.readline())
palindrome(n)