from collections import defaultdict, deque
from copy import deepcopy
global ans,n,m,k,yang,tree

n,m,k = map(int, input().split())
yang = [[*map(int,input().split())] for _ in range(n)]
gg = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    y,x,yr = map(int,input().split())
    gg[y-1][x-1].append(yr)
for i in range(n):
    for j in range(n):
        if gg[i][j] :
            gg[i][j].sort()
            gg[i][j] = deque( gg[i][j] )

dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
g = [[5]*n for _ in range(n)]

def fourseason( gg ):
    ret = [[deque() for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n) :
            killed = 0
            if gg[y][x]:
                now = g[y][x]
                for yr in gg[y][x]:
                    if now >= yr :
                        ret[y][x].append(yr+1); now -= yr
                        if (yr+1) % 5 == 0 :
                            for d in dir:
                                ny,nx = y+d[0], x+d[1]
                                if ny>=0 and nx>=0 and ny<n and nx<n: ret[ny][nx].appendleft(1)
                    else : killed += yr//2
                g[y][x] = now
            g[y][x] += ( yang[y][x] + killed )
    return ret


for kk in range(k): gg = fourseason(gg)

ans = 0
for i in range(n):
    for j in range(n):
        if gg[i][j] : ans+= len(gg[i][j])
print(ans)