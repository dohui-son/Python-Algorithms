from collections import defaultdict, deque
from copy import deepcopy

gg = [ input() for _ in range(12)]
global g
g = [ deque(['.']*12) for _ in range(6)]
tonum = defaultdict(int)
for y,yval in enumerate(gg):
    for x,val in enumerate(yval):g[x][11-y] = val
for i in range(6): tonum[(1<<i)] = i
ans = 0
dir = [(0,1),(-1,0),(1,0),(0,-1)]


def bfs(sy,sx):
    col = g[sy][sx]
    ret = deque([(sy,sx)]); q = deque([(sy,sx)])
    v = deepcopy(visit)

    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = y+d[0],x+d[1]
            if ny<0 or nx<0 or ny>=6 or nx>= 12: continue
            if v[ny][nx] or g[ny][nx] != col : continue
            v[ny][nx] = True
            q.append((ny,nx)); ret.append((ny,nx))
    return ret


def pushpush(bit):
    while bit:
        now = bit&-bit; bit-=now
        y = tonum[now]
        neww = deque()
        for yy in g[y]:
            if yy != '.': neww.append(yy)
        if len(neww)<12: neww.extend(['.']*(12-len(neww)))
        g[y] = neww

while True:
    changed = 0
    visit = [[False]*12 for _ in range(6)]
    flag = False
    for y in range(6):
        for x in range(12):
            if g[y][x] == '.': continue
            elif visit[y][x] == False:
                visit[y][x] = True
                dq = bfs(y,x)
                if len(dq)>=4:
                    flag = True
                    for l in dq:
                        y,x = l
                        visit[y][x] = True
                        g[y][x] = '.'
                        changed |= (1<<y)
    if flag: ans+=1
    else: break
    if changed: pushpush(changed)

print(ans)