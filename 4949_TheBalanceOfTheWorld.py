from sys import stdin


def bracket(data):
    s = []
    for i in data:
        if i == "(" or i == "[":
            s.append(i)
        elif i == ")":
            if len(s) == 0 or s[-1] != "(":
                print("no")
                return
            else:
                s.pop()
        elif i == "]":
            if len(s) == 0 or s[-1] != "[":
                print("no")
                return
            else:
                s.pop()
    if len(s) == 0:
        print("yes")
    else:
        print("no")
    return


while 1:
    data = stdin.readline().strip()
    if data == ".":
        break
    else:
        bracket(data)


