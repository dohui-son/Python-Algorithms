from collections import deque, defaultdict
from copy import deepcopy
n,m= map( int, input().split() )
g = [ [*map(int,input().split())] for  _ in range(n) ]
hoobo = deque(); virus = deque()

ans = 0; safe = 0


for i in range(n):
    for j in range(m):
        if g[i][j] == 0: hoobo.append((i,j)); safe+=1
        elif g[i][j] == 2: virus.append((i,j))
hlen = len(hoobo); dir = [(0,1),(-1,0),(0,-1),(1,0)]

def test():
    global dir, ans
    visit = [[False]*m for _ in range(n) ]
    q = virus.copy()
    anj = safe-3
    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=m: continue
            if g[ny][nx]>0: continue
            if visit[ny][nx] : continue
            visit[ny][nx] = True; anj-=1
            q.append((ny,nx))
    ans = max(ans, anj)

def BT(total,cur):
    if cur>3:return
    if cur == 3: test();return
    elif total > 0:
        bit = total
        while bit:
            smallest = bit&-bit
            idx = bin(smallest)[::-1].index('1')
            y,x = hoobo[idx]
            g[y][x] = 1
            BT(total&(~smallest), cur+1)
            g[y][x] = 0
            bit &= (bit-1)

BT((1<<hlen)-1, 0)
print(ans)