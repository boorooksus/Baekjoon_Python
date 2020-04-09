from sys import stdin, stdout

n = int(stdin.readline()) # n : number of class
a = list(map(int, stdin.readline().split())) #a : number of examinee
#b, c : number of examinee monitored by supervisor/ assistant
b, c = map(int, stdin.readline().split())

cnt = 0
for i in a:
    i -= b
    cnt += 1
    # == 1 ========================
    if i < 0:
        continue
        
    if(i % c == 0):
        cnt += i // c
    else:
        cnt += i // c + 1

print(cnt)



# 1 : b 뺐을 때 음수가 되는 경우도 고려하기