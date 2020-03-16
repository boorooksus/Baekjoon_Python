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
n = 3
d_list = [7, 10, 2]
d_dict = {a + 1:d_list[a] for a in range(n)}
print(d_dict)

