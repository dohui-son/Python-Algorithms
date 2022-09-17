from collections import defaultdict,deque
global n,m, g
n,m = map(int,input().split())
g = [list(input()) for _ in range(n)]
visit = defaultdict(list)

sry,srx,sby,sbx = 0,0,0,0
for y in range(n):
    for x in range(m):
        if g[y][x] == 'B': 
            sby,sbx = y,x
            g[y][x] = '.'
        elif g[y][x] == 'R': 
            sry,srx = y,x
            g[y][x] = '.'
visit[(sry,srx,sby,sbx )] = 1
dir = [(1,0),(-1,0),(0,1),(0,-1)]
direct = [ [2,3], [2,3], [0,1], [0,1], [0,1,2,3] ]
q = deque([(1,4,sry,srx,sby,sbx)])

def playball(d,sy,sx):
    global n,m, g
    y,x = sy,sx
    ret = 0
    
    while g[ y+dir[d][0] ][ x+dir[d][1] ] != '#'  and g[y][x] != 'O'  :
        y,x = y+dir[d][0],x+dir[d][1]
        ret += 1
    if g[y][x] == 'O': return -1,-1, ret
    else : return y, x, ret

def play(d, cnt, ry, rx, by, bx ):
    global n,m, g
    nry,nrx,rcnt = playball(d,ry,rx)
    nby,nbx,bcnt = playball(d,by,bx)
    if nry==-1 and nby>-1: print(cnt);exit(0)

    if nry>-1 and nry == nby and nrx == nbx :
        if rcnt>bcnt: nry -=dir[d][0]; nrx -= dir[d][1]
        else: nby -=dir[d][0]; nbx -= dir[d][1]
    return nry,nrx,nby,nbx

while q:
    cnt,pre,ry,rx,by,bx = q.popleft()
    if cnt>=11: continue
    for d in direct[pre]:
        nry,nrx, nby, nbx = play(d, cnt, ry, rx, by, bx )
        if nry == -1 and nrx == -1 and nby == -1 and nbx == -1: continue
        if visit[(nry,nrx,nby,nbx )] : continue
        visit[(nry,nrx,nby,nbx )] = 1
        q.append((cnt+1, d, nry,nrx, nby,nbx))

print(-1)            