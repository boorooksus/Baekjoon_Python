'''n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
for i in range(n - 1, 0, -1):
    #상향식 힙정렬
    for j in range(i, 0, -1):
        if num[j] > num[(j - 1) / 2]:
            temp = num[j]
            num[j] = num[(j - 1) / 2]
            num[(j - 1) / 2] = temp

        temp = num[0]
        num[0] = num[i]
        num[i] = temp

for i in range(n):
    print(num[i])'''
def quickSort(data, start, end):
    if start >= end: return
    key = start
    i = start + 1
    j = end
    while i <= j:
        while i <= end and data[i] <= data[key]:
            i += 1
        while j > start and data[j] >= data[key]:
            j -= 1
        if i > j:
            temp = data[j]
            data[j] = data[key]
            data[key] = temp
        else:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
    quickSort(data, start, j - 1)
    quickSort(data, j + 1, end)

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
quickSort(num, 0, n)
print(num)