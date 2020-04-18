from sys import stdin

word = stdin.readline().strip()
reverse = str()
for i in range(len(word) - 1, -1, -1):
    reverse += word[i]
if word == reverse:
    print(1)
else:
    print(0)
    
#문해기 5주차 1번 유형