from sys import stdin
from collections import deque

word = stdin.readline().strip()

def palindrome(word):
    cnt_list = [0 for i in range(26)]
    for i in word:
        cnt_list[ord(i) - 65] += 1

    ans_front = []
    ans_back = []

    save = '0'
    for i in range(26):
        if cnt_list[i] % 2 == 1:
            if len(word) % 2 == 0 or save != '0':
                #======== 1 ==============================
                print("I'm Sorry Hansoo")
                return
            save = chr(i + 65)
        for _ in range(cnt_list[i] // 2):
            ans_front.append(chr(i + 65))
            ans_back.insert(0, chr(i + 65))

    if save != '0':
        ans_front.append(save)

    for i in ans_front:
        print(i, end='')
    for i in ans_back:
        print(i, end='')


palindrome(word)

#문해기 5주차 1번 문제 유형
# 1 : sorry로 썼다가 틀림
