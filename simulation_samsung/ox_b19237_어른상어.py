# 어른상어 - 2시간
from collections import deque, defaultdict

dir = [(-1,0),(1,0),(0,-1),(0,1)]
n,m,k = map(int,input().split())
gg = [[*map(int,input().split())] for _ in range(n)]
fdir = [*map(int,input().split())]
sdir = []
g = [[[0,0,0] for _ in range(n)] for _ in range(n)]

for mm in range(m):
    l = []
    for _ in range(4):l.append([*map(int,input().split())])
    sdir.append(l)
shark = defaultdict(list)
for y in range(n):
    for x in range(n):
        if gg[y][x] :
            shark[gg[y][x]] = [y,x,fdir[ gg[y][x]-1 ] ]
            g[y][x][0] = gg[y][x]

smell = deque()
nowshark = [i for i in range(1,m+1)]
for tt in range(1,1001):

    tmp_s = nowshark.copy()
    visit = 0
    dead = 0
    for snum in tmp_s:
        visit |= ( 1 << snum )
        y,x,d = shark[snum]

        g[y][x][1] = snum; g[y][x][2] = k; smell.append((y,x)) # 냄새뿌리기

        biny,binx,myy,myx,nd, myd,eat = -1,-1,-1,-1,-1,-1, False
        for dd in sdir[snum-1][d-1]:
            nd, ny, nx = dd, y+dir[dd-1][0], x+dir[dd-1][1]

            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if g[ny][nx][1]>0 and g[ny][nx][1]!=snum: continue

            if g[ny][nx][0] == 0 and g[ny][nx][1] == snum and myy == -1 : myy = ny; myx = nx; myd=nd
            if g[ny][nx][0] == 0 and g[ny][nx][1] == 0 : biny = ny; binx = nx; break
            if g[ny][nx][0]>0 and visit & (1<<g[ny][nx][0]) : # 이동이미 했는 상어라서 같은 칸에 있게 되는
                eat = True; biny = ny; binx = nx;break
        if biny > -1:
            if eat:
                if g[biny][binx][0] < snum:
                    del shark[snum] # 나 죽엇다
                    dead |= (1<<snum)
                    nowshark.remove(snum)
                    g[y][x][0] = 0
                    continue
                else:
                    del shark[ g[biny][binx][0] ] ## 먼저 칸에 들어와있는 애를 죽여야함
                    nowshark.remove( g[biny][binx][0] )
                    dead |= (1<< g[biny][binx][0])

            g[y][x][0] = 0
            g[biny][binx][0] = snum
            shark[snum] = [biny, binx,nd]

        elif myy > -1:
            g[y][x][0] = 0
            g[myy][myx][0] = snum
            shark[snum] = [myy,myx,myd]

    if len(nowshark) == 1: print(tt); exit(0)
    tmp = smell.copy()
    smell = deque()
    visit = [ [False]*n for _ in range(n)]
    for s in tmp:
        y,x = s
        if visit[y][x]: continue
        visit[y][x] = True

        if g[y][x][2]>0:
            g[y][x][2] -= 1
            if g[y][x][2] > 0 : smell.append((y,x))
            else: g[y][x][1] = 0

print(-1)