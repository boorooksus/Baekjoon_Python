s = input()
alp = [-1] * 26
for i in range(len(s)):
    index = ord(s[i]) - 97
    if alp[index] == -1:
        alp[index] = i
for i in alp:
    print(i, end=' ')