word = input()
sec = 0
for i in word:
    ascii = ord(i)
    if ascii < 80:
        sec += (ascii - 65 + 9) // 3
    elif ascii < 84:
        sec += 8
    elif ascii < 87:
        sec += 9
    else:
        sec += 10
print(sec)