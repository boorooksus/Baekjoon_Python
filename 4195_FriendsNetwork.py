from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10**9)

def getParent(a, friendRoot):
    if a == friendRoot[a]: return a
    friendRoot[a] = getParent(friendRoot[a], friendRoot)
    return friendRoot[a]

def unionParent(a, b, friendRoot, friendCnt):
    a = getParent(a, friendRoot)
    b = getParent(b, friendRoot)
    temp = friendCnt[b]
    friendCnt[a] += friendCnt[b]
    friendCnt[b] += temp
    if a > b:
        friendRoot[a] = b

    else: friendRoot[b] = a
    return

'''def findFriends(a, friendRoot):
    root = getParent(a, friendRoot)
    friendRoot_list = list(friendRoot.values())
    for i in range(len(friendRoot_list)):
        friendRoot_list[i] = getParent(friendRoot_list[i], friendRoot)
    return friendRoot_list.count(root)'''


#테스트 케이스
t = int(stdin.readline())

for i in range(t):
    friendRoot = {} #친구가 속해있는 그룹의 부모를 저장하는 딕셔너리
    friendCnt = {}
    f = int(stdin.readline()) #친구 관계 수
    for j in range(f):
        a, b = stdin.readline().split()
        #딕셔너리에 해당 아이디가 없을 경우 데이터 추가
        if a not in friendRoot:
            friendRoot[a] = a
            friendCnt[a] = 1
        if b not in friendRoot:
            friendRoot[b] = b
            friendCnt[b] = 1
        #부모 합치기
        unionParent(a, b, friendRoot, friendCnt)
        print(friendCnt[getParent(a, friendRoot)])


