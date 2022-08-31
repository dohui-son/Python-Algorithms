# 12:55
from collections import deque
global k,n,m
t = int(input().rstrip())
gg = []
dir = [(0,1),(1,0),(-1,0),(0,-1)]
k,n,m = 0,0,0
def dfs(y,x):
    global k,n,m
    k-=1
    if k == 0: return
    for d in dir:
        ny,nx = d[0]+y, d[1]+x
        if ny<0 or nx<0 or ny>=n or nx>=m: continue
        if g[ny][nx] :
            g[ny][nx] = 0
            dfs(ny,nx)

for tt in range(t):
    m,n,k = map(int,input().split())
    g = [[0]*m for _ in range(n)]
    ans = 0
    bachoo = deque([])
    for _ in range(k):
        x,y = map(int,input().split())
        print("now",y,x)
        g[y][x] = 1
        bachoo.append((y,x))

    for b in bachoo:
        if g[b[0]][b[1]] == 1:
            ans+=1
            g[b[0]][b[1]] = 0
            dfs( b[0], b[1])
            if k == 0: break
    print(ans)