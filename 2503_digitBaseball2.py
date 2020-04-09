from sys import stdin

def cases(n):
    ans = []
    comp_list = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and j != k and k != i:
                    comp_list.append(100 * i + 10 * j + k)

    for i in comp_list:
        isTrue = True
        for j in range(n):
            if meet(i, cdt[j][0], cdt[j][1], cdt[j][2]) == False:
                isTrue = False
        if isTrue == True:
            ans.append(i)

    print(len(ans))
    #print(ans)

def meet(comp, number, strike, ball):
    comp_list = list(int(i) for i in str(comp))
    num_list = list(int(i) for i in str(number))
    st = 0
    ba = 0
    for i in range(3):
        if comp_list[i] == num_list[i]:
            st += 1
    '''comp_list.sort()
    num_list.sort()
    for i in range(3):
        if comp_list[i] == num_list[i]:
            ba += 1'''
    for i in comp_list:
        if i in num_list:
            ba += 1
    ba -= st
    if st == strike and ba == ball:
        return True
    else:
        return False

n = int(stdin.readline())
cdt = []
for i in range(n):
    cdt.append(list(map(int, stdin.readline().split())))
cases(n)

