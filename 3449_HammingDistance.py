from sys import stdin

t = int(stdin.readline())
for i in range(t):
    a = stdin.readline()
    b = stdin.readline()
    hamming = 0
    for j in range(len(a)):
        if a[j] != b[j]:
            hamming += 1
    print("Hamming distance is %s." %hamming)