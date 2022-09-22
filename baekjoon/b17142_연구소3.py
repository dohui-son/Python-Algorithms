from collections import defaultdict,deque
from itertools import combinations
global n,m,info,ans,zero,vlen
n, m = map(int,input().split())
info = [[*map(int, input().split())] for _ in range(n)]
ans = n*n+1
zero = 0

virus = deque(); vlen = 0
for y in range(n):
    for x in range(n):
        if info[y][x] == 2: 
            virus.append((y,x))
            vlen += 1
        elif info[y][x] == 0: zero+=1

if zero == 0: print(0);exit(0)
if len(virus) == 0 and zero>0: print(-1);exit(0)

dir = [(0,1),(0,-1),(1,0),(-1,0)]
def spread(q):
    global n,m,info,ans,zero,vlen
    z,time,maxi = 0, 0, 0
    v = [[-1]*n for _ in range(n)]
    while q:
        l = q.popleft()
        y,x,time = l[0], l[1], 0
        if v[y][x] == -1:v[y][x] = 0
        if len(l) > 2: time = l[2]
        
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if info[ny][nx] == 1 or v[ny][nx]>-1: continue
            v[ny][nx] = time+1
            if info[ny][nx] == 0 :
                if v[ny][nx] > ans: return
                z += 1
                maxi = max(v[ny][nx], maxi)            
            q.append((ny,nx, time+1))

    if zero == z:ans = min(maxi, ans)
    else: return

if len(virus) < m : spread(virus)            
else:
    combi = combinations( virus, m)
    for c in combi: spread(deque(c))
print( -1 if ans == n*n+1  else ans)