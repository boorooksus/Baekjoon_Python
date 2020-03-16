a, b = map(list, input().split())
a.reverse()
b.reverse()
ra = int(''.join(a))
rb = int(''.join(b))

print(ra if ra > rb else rb)