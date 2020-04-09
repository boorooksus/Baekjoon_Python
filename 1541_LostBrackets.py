from sys import stdin

formula = stdin.readline()
num = [] #식의 숫자들 저장
oprt = [] #식의 연산자 저장

#식의 숫자와 연산자를 구분해서 각각의 리스트에 저장함
cur = 0
for i in formula:
    if i == '+' or i == '-' or i == '\n':
        num.append(cur)
        oprt.append(i)
        cur = 0
    else:
        cur = cur * 10 + int(i)

#식에 모두 덧셈만 있으면 다 더하기만 하면 됨
if '-' not in oprt:
    ans = sum(num)
# ====== 1 ==============================

else:
    # ===2 ==================================
    #덧셈 연산을 먼저 모두 수행한다
    idx = 0
    while '+' in oprt:
        if oprt[idx] == '+':
            num[idx] += num[idx + 1]
            del num[idx + 1]
            del oprt[idx]
            # == 3 ===========================
            idx -= 1
        idx += 1
    #덧셈 모두 한 후 뺄셈 수행
    ans = num[0] - sum(num[1:])

print(ans)


#그리디 알고리즘
#1: 쓸데없이 아래 코드 추가했다가 틀림
'''elif '+' not in oprt:
    ans = -sum(num)'''
#2 : 아래처럼 했다가 런타임 에러남 + "while '+' not in oprt" 이렇게 했다가 런타임 에러남
'''else:
    while '+' in oprt:
        for i in range(len(oprt) - 1):
            if oprt[i] == '+':
                num[i] += num[i + 1]
                del num[i + 1]
                del oprt[i]'''

#이거 안써서 런타임 에러남
