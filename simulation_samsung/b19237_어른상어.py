#어른상어 2시
from collections import defaultdict,deque

global n,m,k,g,shark,sdir,smell

# INITIALIZE
shark = defaultdict(list)
dir = [(-1,0), (1,0), (0,-1), (0,1)] # 위, 아래, 왼쪽, 오른쪽
n,m,k = map(int ,input().split())
gg = [[*map(int,input().split())] for _ in range(n)]
g = [[[0,0]  for _ in range(n)] for _ in range(n)]
initial = [*map(int, input().split())]
sdir = defaultdict(list)
smell = deque()
for mm in range(m):
    for i in range(4):
        l = [*map(int, input().split())]
        sdir[mm+1].append( (l[0]-1, l[1]-1 , l[2]-1, l[3]-1) )
for y in range(n):
    for x in range(n):
        if gg[y][x] != 0 :
            shark[ gg[y][x] ] = [y,x,initial[ gg[y][x]-1 ] -1 ]
            g[y][x] = [k, gg[y][x]]
            smell.append((y,x))

# 상어 이동
def sharkmove():
    global n, m, k, g, shark, sdir, smell
    sg = [[0] * n for _ in range(n)]
    keylist = list( shark.keys() )
    neww = deque()

    for snum in keylist:
        y,x,sd = shark[snum]
        yxd = [[-1,-1,-1] for _ in range(2) ]


        for d in sdir[snum][sd]:
            ny,nx = y+dir[d][0], x+dir[d][1]
            if ny<0 or nx<0 or ny>= n or nx>=n: continue
            if g[ny][nx][0] == 0 or (ny, nx) in neww  : yxd[0] = [ny, nx, d]; break
            elif  g[ny][nx][0] >0 and g[ny][nx][1] == snum:
                if yxd[1][0]==-1: yxd[1] = [ny,nx,d]

        for i in range(2):
            yy,xx,dd = yxd[i]
            if yy > -1:
                if sg[yy][xx]>0 and sg[yy][xx] < snum: del shark[snum]
                else:
                    if sg[yy][xx] > 0 and sg[yy][xx] > snum : del shark[sg[yy][xx]] # 다른 상어 잡아먹기
                    g[yy][xx] = [k+1, snum]
                    if not (yy,xx) in smell : smell.append( (yy,xx) )
                    shark[snum] = [yy,xx,dd]
                    sg[yy][xx] = snum
                    if i == 0: neww.append((yy,xx))
                break

for time in range(1000) :
    sharkmove()

    # 냄새 1씩 줄이기
    if smell :
        pre = smell.copy()
        for l in pre:
            y,x = l
            if g[y][x][0] >0 : g[y][x] = [g[y][x][0]-1, g[y][x][1] ]
            if g[y][x][0] == 0: smell.remove((y,x)); g[y][x] = [0 , 0]

    if len(shark) == 1: print(time+1);exit(0)
print(-1)