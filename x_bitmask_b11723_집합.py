import sys ;reader = sys.stdin.readline
m = int(reader().rstrip())
bit = 0
for i in range(m):
    l = list(reader().split())
    if l[0] == 'all' : bit = (1<<21)-1 # 20이 아니라 21임에 유의해야함
    elif l[0] == 'empty' : bit = 0
    elif l[0] == 'add' : bit |=  (1 << int(l[1]))
    elif l[0] == 'remove' : bit &= ~(1<< int(l[1]))
    elif l[0] == 'check' : print(1) if bit & (1<<int(l[1])) else print(0)
    elif l[0] == 'toggle' : bit ^= (1<<int(l[1]))