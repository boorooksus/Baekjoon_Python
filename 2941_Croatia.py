word = input()
count = 1
for i in range(1, len(word)):
    if word[i] == '=' or word[i] == '-':
        if i > 1:
            if word[i - 2] == 'd' and word[i - 1] == 'z':
                count -= 1
        count -= 1
    elif word[i] == 'j' and word[i-1] == 'l':
        count -= 1
    elif word[i] == 'j' and word[i - 1] == 'n':
        count -= 1
    count += 1
print(count)
