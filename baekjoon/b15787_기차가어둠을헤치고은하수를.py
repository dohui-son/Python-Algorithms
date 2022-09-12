from collections import defaultdict, deque

n,m = map(int,input().split())
t = [0]*n
i,x = 0,0
for _ in range(m):
    l = [*map(int, input().split())]
    i = l[1]-1
    if l[0]<3: x = l[2]-1

    if l[0] == 1 : t[i] |= ( 1<<x )
    elif l[0] == 2 : t[ i ] &= ~( 1<<x )
    elif l[0] == 4 : t[ i ] = (t[ i ]>>1)
    elif l[0] == 3 : 
        t[ i ] &= ~( 1<<19 )
        t[ i ] = (t[ i ]<<1)

print(len(set(t)))