# 연구소3
from itertools import  combinations
from collections import defaultdict, deque
n,m = map(int,input().split())
g = [ list(map(int,input().split())) for _ in range(n) ]
v = []; ans = int(2e9)
cnt = 0
for i in  range(n):
    for j in range(n):
        if g[i][j] == 2: v.append((i,j))
        elif g[i][j] == 0: cnt += 1
arr = [i for i in range(len(v))]
combi = []
if cnt == 0: print(0);exit()
dir = [(0,1), (0,-1), (1,0), (-1,0)]
if len(v) < m: combi = [arr]
else: combi = list(combinations(arr,m))
for co in combi:
    q = deque()
    c = [[-1] * n for _ in range(n)]
    for i in co:
        q.append([ v[i][0], v[i][1],0]); c[v[i][0]][v[i][1]] = 0

    while q:
        y,x,cost = q.popleft()

        for d in dir:
            ny, nx = y+d[0],x+d[1]
            if ny<0 or ny>=n or nx<0 or nx>=n: continue
            if g[ny][nx] == 1: continue
            if c[ny][nx] == -1:
               if g[ny][nx] == 2: c[ny][nx] = c[y][x]; q.append([ny,nx,cost+1])
               else:  c[ny][nx] = cost+1; q.append([ny,nx,cost+1])
    minus = False; maxi = 0
    for i in  range(n):
        if minus:break
        for j in range(n):
            if c[i][j] == -1 and g[i][j] == 0: minus=True;break
            elif c[i][j] == -1 and g[i][j] == 2: minus = True;break
            elif c[i][j]>-1: maxi = max(maxi, c[i][j])
    if minus == False: ans = min(ans, maxi)

print(-1) if ans == int(2e9) else print(ans)


