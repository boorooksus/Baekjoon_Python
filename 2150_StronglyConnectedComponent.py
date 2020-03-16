from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

v, e = map(int, stdin.readline().split())

#connection = [[0]] * (v + 1) #노드의 연결 관계 저장
connection = []
for i in range(v + 1):
    connection.append([0])
id = 0 #정점의 아이디
d = [0] * (v + 1) #각 정점의 아이디를 저장하는 리스트
stack = [] #스택
finished = [False] * (v + 1) #처리중인지 확인(True이면 처리 완료)
SCC = [] #같은 SCC에 속한 정점 리스트를 저장하는 리스트

def dfs(x):
    global id
    id += 1
    d[x] = id #고유 아이디를 저장
    stack.append(x) #스택에 자기 자신을 삽입

    parent = d[x]
    for i in range(1, len(connection[x])):
        y = connection[x][i]
        #탐색 안된 노드 일 때
        if d[y] == 0:
            parent = min(parent, dfs(y))
        #처리중인 노드 일 때
        elif finished[y] == False:
            parent = min(parent, d[y])

    if parent == d[x]: #부모가 자기 자신일 때
        scc = []
        while(1):
            t = stack[-1]
            stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)

    return parent

#간선 정보 입력
for i in range(e):
    x, y = map(int, stdin.readline().split())
    #connection[x] = connection[x] + [y]
    connection[x].append(y)

#SCC 찾기
for i in range(1, v + 1):
    if d[i] == 0:
        dfs(i)

print(len(SCC)) #SCC 개수 출력

#SCC 데이터를 오름차순으로 정렬
for i in range(len(SCC)):
    SCC[i].sort()
SCC.sort()

for i in range(len(SCC)): #SCC에 속한 정점 출력
    print(*SCC[i], end=" -1\n")