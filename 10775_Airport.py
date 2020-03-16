from sys import stdin

def isOccupied(gate):
    for i in range(gate - 1, 0, -1):
        if gates_list[i] == -1:
            return i
    return -1

def moveLeft(emp, gate):
    for i in range(emp, gate):
        gates_list[i] = gates_list[i + 1]
    return

g = int(stdin.readline()) #number of gates
p = int(stdin.readline()) #number of planes
planes_list = []
gates_list = [-1 for i in range(g + 1)]
cnt = 0
for i in range(p):
    gate = int(stdin.readline())
    planes_list.append(gate)
    emp = isOccupied(gate)
    if gates_list[gate] == -1:
        gates_list[gate] = i
        cnt += 1
    elif emp != -1:
        moveLeft(emp, gate)
        gates_list[gate] = i
        cnt += 1
    else:
        for j in range(g + 1):
            gates_list[j] = 10
print(cnt)


