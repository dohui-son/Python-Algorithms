#미세먼지 안녕 #1시간 41분
from collections import deque, defaultdict
r,c,t = map(int, input().split())
g = [list(map(int,input().split())) for _ in range(r)]
air = [] ; dir = [(0,1),(0,-1),(1,0),(-1,0)]
mise = deque()
for i in range(r):
    for j in range(c):
        if g[i][j] == -1 : air.append( (i, j) )
        if g[i][j]>0 : mise.append( [ i, j, g[i][j]] ); g[i][j] = 0


def purifier(pdx, g):
    dirr = [ [(0,1),(-1,0),(0,-1),(1,0)] ,[(0,1),(1,0),(0,-1), (-1,0) ] ]
    sy , sx = air[pdx]; now_dir = 0
    y = sy; x = sx+1; ny, nx, pre = 0,0,0
    while True:
        ny = dirr[pdx][ now_dir][0] + y
        nx = dirr[pdx][now_dir ][1] + x
        if ny<0 or nx<0 or ny>=r or nx>=c : now_dir += 1 ; continue
        if g[y][x] == -1: break
        g[y][x], pre = pre, g[y][x]   #이부분이 문제였음****************
        y, x = ny,nx

while t:
    while mise: # 미세먼지퍼짐 -> 이 작업전에 g는 비어있었음
        y, x, amount = mise.popleft()
        sp_cnt = 0
        for d in dir:
            ny, nx = d[0]+y, d[1]+x
            if ny<0 or nx<0 or ny>=r or nx>=c:continue
            if g[ny][nx] == -1:continue
            sp_cnt += 1
            g[ny][nx] += amount//5
        g[y][x] += ( amount - (amount//5)*sp_cnt )

    purifier(0, g)
    purifier(1, g)

    for i in range(r):
        for j in range(c):
            if g[i][j]>0: mise.append([i,j,g[i][j]]); g[i][j] = 0
    t-=1
ans = 0
for l in mise: ans += l[2]
print(ans)