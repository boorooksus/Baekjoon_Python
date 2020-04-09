from sys import stdin

def cases(number, strike, ball):
    num = list(int(i) for i in str(number))
    #num = str(number)
    num_list = []
    if strike == 3:
        #return [int("".join(map(str, num)))]
        return [number]
    elif strike == 2:
        for i in range(3):
            for j in range(1, 10):
                if num[i] == j:
                    continue;
                num[i] = j
                num_list.append(int("".join(map(str, num))))
        return num_list
    elif strike == 1 and ball == 2:
        for i in range(3):
            temp = num[(i + 1) % 3]
            num[(i + 1) % 3] = num[(i + 2) % 3]
            num[(i + 2) % 3] = temp
            num_list.append(int("".join(map(str, num))))
        return num_list
    elif strike == 1 and ball == 1:
        '''for i in range(3):
            num[(i + 2) % 3] = num[(i + 1) % 3]
            num_list.append(num)'''

        


    

n = int(stdin.readline()) #n : number of questions
for i in range(n):
