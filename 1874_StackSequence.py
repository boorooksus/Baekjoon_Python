from sys import stdin
from collections import deque

n = int(stdin.readline())
sequence = deque()
#sequence = []
s = []
ans = []
for _ in range(n):
    sequence.append(int(stdin.readline()))

for i in range(1, n + 2):
    if len(s) == 0 or s[-1] != sequence[0]:
        s.append(i)
        ans.append("+")
    elif s[-1] == sequence[0]:
        while len(sequence) != 0 and len(s) != 0 and s[-1] == sequence[0]:
            ans.append("-")
            s.pop()
            sequence.popleft()
        s.append(i)
        ans.append("+")
s.pop()
ans.pop()
if len(sequence) != 0:
    print("NO")
else:
    for i in ans:
        print(i)
