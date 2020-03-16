'''n = input()
n = sorted(n, reverse=True)
print(''.join(n))'''

import sys
n = sys.stdin.readline()
n = sorted(n, reverse=True)
print(''.join(n))