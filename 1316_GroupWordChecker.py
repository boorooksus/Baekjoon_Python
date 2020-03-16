n = int(input())
gr = 0
for i in range(n):
    isgr = 1
    word = input()
    alp = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            if word[i - 1] in alp:
                alp = alp.replace(word[i - 1], "0")
            else:
                isgr = 0
                break
    if word[-1] not in alp:
        isgr = 0

    if isgr == 1:
        gr += 1

print(gr)