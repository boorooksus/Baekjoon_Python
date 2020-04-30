from sys import stdin

a, b = map(int, stdin.readline().split())

gcd = a
while(gcd > 1):
    if gcd <= b and b % gcd == 0 and a % gcd == 0:
        break
    else:
        gcd -= 1
print(gcd)
lcm = gcd * (a // gcd) * (b // gcd)

# === 1 ======================================
'''i = 1
while(lcm < a * b):
    if lcm >= a and lcm >= b and\
            lcm % a == 0 and lcm % b == 0:
        break
    else:
        i += 1
        lcm = gcd * i'''

print(lcm)

# 1 : 이렇게 하면 시간 초과