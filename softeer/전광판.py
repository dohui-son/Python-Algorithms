# 맞았음
import sys 
sys.setrecursionlimit(5000)
from collections import deque, defaultdict
reader = sys.stdin.readline
num = defaultdict(int)
num[0] = (  (1<<0) | (1<<1) | (1<<2) | (1<<3) | (1<<4)  | (1<<5) ) 
num[1] = ( (1<<1) | (1<<2) )
num[2] = ( (1<<0) | (1<<1) | (1<<6) | (1<<3) | (1<<4) )
num[3] = ( (1<<0) | (1<<1) | (1<<6) | (1<<3) | (1<<2) )
num[4] = ( (1<<1) | (1<<2) | (1<<5) | (1<<6) )
num[5] = ( (1<<0) | (1<<2) | (1<<3) | (1<<5) | (1<<6) )
num[6] = ( (1<<0) | (1<<2) | (1<<3) | (1<<4) | (1<<5) | (1<<6) )
num[7] = ( (1<<1) | (1<<2) | (1<<5) | (1<<0) )
num[8] = (1<<7)-1 
num[9] = ( (1<<7)-1 ) ^ (1<<4)


n = int(reader().rstrip())
ans = [7*5]*n
for i in range(n):
    a, b = reader().split()
    ast = ' '*(5-len(a)) + a
    bst = ' '*(5-len(b)) + b
    ans = 0
    for i in range(5):
        if ast[i] == ' ' and bst[i] == ' ': continue
        elif ast[i] == ' ' : ans += bin( num[ int(bst[i]) ] ).count('1')
        elif bst[i] == ' ' : ans += bin( num[ int(ast[i]) ] ).count('1')
        else:ans += bin( num[ int(ast[i]) ] ^ num[ int(bst[i]) ]).count('1')
    print(ans)