import sys

while True:
    try:
        text = sys.stdin.readline()
        newText = text[4:]
        print(newText, end='')
    except:
        break
