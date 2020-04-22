from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n, m = map(int, stdin.readline().split())

module = []
visit = [[0 for _ in range(n)] for _ in range(m)]
roomSize = [0]
roomId = 0



def dfs(y, x, id):
    if visit[y][x] != 0:
        return
    visit[y][x] = id
    roomSize[id] += 1

    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= 0 and ny < m and nx >= 0 and nx < n:
            if len(bin(module[y][x])) > i + 2 and bin(module[y][x])[-i - 1] == '1':
                continue
            dfs(ny, nx, id)


for i in range(m):
    module.append(list(map(int, stdin.readline().split())))

for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            roomId += 1
            roomSize.append(0)
            dfs(i, j, roomId)

print(roomId)
print(max(roomSize))


# =============== 1 =====================
roomSize = [0]
roomId = 0
for i in range(m):
    for j in range(n):
        visit = [[0 for _ in range(n)] for _ in range(m)]
        for k in range(4):
            if len(bin(module[i][j])) > k + 2 and bin(module[i][j])[-k - 1] == '1':
                module[i][j] -= 2 ** k
                roomId += 1
                roomSize.append(0)
                dfs(i, j, roomId)
                module[i][j] += 2 ** k

print(max(roomSize))


#문해기 4주차 유형
# 1 : 벽을 하나하나 부숴볼 때마다 방의크기 재서 답 얻어낸다.