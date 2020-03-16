from sys import stdin

def asciiList(x):
    ascii_list = []
    for i in x:
        ascii_list.append(ord(i))
    return ascii_list

n = int(stdin.readline())
words = []
for i in range(n):
    words.append(stdin.readline())
words = list(set(words))
words.sort(key= lambda x: (len(x), asciiList(x)))

for i in words:
    print(i, end="")
print(words)
#aab aac