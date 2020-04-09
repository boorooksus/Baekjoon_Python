'''
print("Hello World")

tuple = (1, 2, 3)
print(tuple)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple = (list1, list2)
print(tuple[1])
print("Hello\nWorld")


a = int(input())
b = int(input())
print(a + b, a - b, sep='\b\b')
'''

#f = open("input.txt", "r", encoding="UTF-8")
#f.seek(3)
'''
l = f.readlines()
for i, l in enumerate(l):
    print("%s번째 줄: %s" %(i, l), end='')
data = f.read()
for i in data:
    print(i)
f.close()
'''


'''t = (1, 2, (3, 4))
print(t[2][0])

#for i in range(65, 91):
#    print("\'%s\' : 0, "%(chr(i)), end='')

v = list(range(10))
print([i for i in v])
print(", ".join(str(i) for i in v))

word = 'aabbba'
print(sorted(word, key=word.find))
print(list(word))

list1 = [1, 2, 3]
list2 = [1, 2, 4]
list3 = [list2, list1]
list3.sort()
print(list3)'''


'''from sys import stdin
n = int(stdin.readline())
members = []
for i in range(n):
    members.append(stdin.readline().split())
for i in enumerate(members):
print(members)'''

'''def func(list1):
    list1[0] = 1

list1 = [0, 0, 0]
func(list1)
print(list1)
print(list1.count(3))

n = 10
arr = [i+1 for i in range(n)]
print(arr)'''

'''arr = [] * 10
arr[0] = 1
print(arr[0])'''

'''padovan_list = [-1, 1, 1, 1, 2]
padovan_list.append(-1 for i in range(5, 10))
print(padovan_list)'''

#print(int(round( 3/ 2, 0)))

#arr = [[1, 2, 3], [4, 5]]
#print(*arr[1],end='')
#print("Hello")
#print(arr[-1])

'''from sys import stdin

for i in range(3):
    x, y = map(int, stdin.readline().split())
    arr[x].append(y)
print(arr)'''

'''arr = [[0] for i in range(3)]
print(arr)
col_str = "1 2 3"
col_list = col_str.split(' ')
for j in col_list:
    arr[1].append(int(j))
print(arr)'''

'''a = []
a.append(int(input().split()))
print(a)'''

'''parent = {i:i + 1 for i in range(5)}
print(parent[1])'''

from sys import stdin
#a, b = stdin.readline().split()


'''dic = {'a': 'afdag', 'b' : 'bsdgdsagd'}
print(dic['a'])
dic_list = list(dic.values())
print(dic_list[1])'''

'''a = []
a.append(int(input()))
print(a)'''

'''gates_list = [0, 1, 2, 3, 4, 5]
for i in range(0, 4):
    gates_list[i] = gates_list[i + 1]
print(gates_list)'''

'''arr = [[1,2], [3, 4, 5]]
print(len(arr[1]))'''

'''arr = list(map(int, input().split()))
print(arr)'''

'''t = input()
case = 1
while(1):
    a = input()
    b_list = list(input().split())
    n = int(input())
    change = []
    for i in range(n):
        change = list(map(int, input().split()))
    print("case %s :"%case, a, b_list, n, change)
    case += 1'''
'''n = 3
d_list = [7, 10, 2]
d_dict = {a + 1:d_list[a] for a in range(n)}
print(d_dict)'''

'''import queue
q = queue.Queue()
q.put([1, 2])
x = q.get()
print(x[1])'''

'''arr = []
arr.append(list(map(int, str(stdin.readline().strip()))))
print(arr)'''

'''maze = []
maze.append(list(map(int, str(input()))))
print(maze)'''

'''import queue
q = queue.Queue()
q.put(3)

def func():
    x = q.get()
    print(x)
    return

func()'''

'''from collections import deque
q = deque()
q.append(3)
print(len(q))
x = q.pop()
print(x)'''

'''h = 3
n = 3
container = []
for i in range(h):
    layer = []
    for j in range(n):
        layer.append(list(map(int, stdin.readline().split())))
    container.append(layer)

print(container)'''

'''from collections import deque
q = deque()
q.appendleft(1)
q.appendleft(2)
print(list(q))
a = q.pop()
print(q)
print(a)'''

'''l = ['1', '2', '3']
i = int("".join(l))
print("".join(l))
print(i)

splitted_str = ['Hi', 'my', 'name', 'is', 'limcoing']

joined_str = "-".join(splitted_str)
print(joined_str)

num = [1, 2, 3]
print([int("".join(map(str, num)))])'''

'''cdt = []
cdt.append(list(map(int, stdin.readline().split())))
print(cdt)'''

'''def meet(comp, number, strike, ball):
    comp_list = list(int(i) for i in str(comp))
    num_list = list(int(i) for i in str(number))
    st = 0
    ba = 0
    for i in range(3):
        if comp_list[i] == num_list[i]:
            st += 1
    for i in comp_list:
        if i in num_list:
            ba += 1
    ba -= st
    if st == strike and ba == ball:
        return True
    else:
        return False

comp = 324
number = 123
strike = 1
ball = 1
print(meet(comp, number, strike, ball))'''

'''blank = [' ', ' ', ' ']
print(*blank)'''

'''a = [0]
b = [1, 2, 3]
print(b + a)'''

'''import sys

num = int(input())

def star(i, j):
    while(i != 0):
        if i == 4 and j == 3:
            abcdef = 0
        # 몫이 1인 경우
        if(i % 3 == 1 and j % 3 == 1):
            sys.stdout.write(' ')
            return None
        # 3으로 나누어서 위의 if문에 걸리면 그 부분도 빈칸 처리
        i = i // 3
        j = j // 3
    sys.stdout.write('*')

for i in range(num):
    for j in range(num):
            star(i, j)
    sys.stdout.write('\n')'''

'''a = 3
print("Hi%s"%a)'''

'''from sys import stdin

a = []
n = int(stdin.readline())
for i in range(n):
    a.append(int(stdin.readline()))

a.sort()
for i in range(n):
    print(a[i])'''

'''count = [0 for i in range(10001)]
n = int(stdin.readline())
for i in range(n):
    idx = int(stdin.readline())
    count[idx] += 1

for i in range(10001):
    cnt = count[i]
    for j in range(cnt):
        print(i)'''

'''q = [0, 1, 2, 3, 3, 3]
q.remove(max(q))
print(q)'''

'''string = [sum([int(plus) for plus in minus.split('+')]) for minus in input().split('-')]
print(string[0] - sum(string[1:]))'''

'''arr = [[[7, 4], [1, 2], [3, 7]], [[2, 7], [7, 5]]]
idx = 0
if 5 in arr[1:2]:
    idx =  arr[1:2].index(5) + 1
print(idx)'''

'''import heapq
pq = []
heapq.heappush(pq, (2,3))
heapq.heappush(pq, (3,4))

a, b = heapq.heappop(pq)
print(a)'''

'''for _ in range(5):
    print("first", _)
    for _ in range(2):
        print("check", _)'''
arr = [5, 2, 3]
ans = min(arr)
print(ans)
