# 1시간 45분
from collections import defaultdict, deque
global sharkdir, fishcnt

g = [[[deque(), deque()] for _ in range(4)] for _ in range(4)]
smell = [[0]*4 for _ in range(4)]
shy, shx, ans = 0, 0 , 0
#         ←,      ↖,      ↑,     ↗,     →,     ↘,     ↓,     ↙
dir = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

m, S = map(int ,input().split())
for mm in range(m):
    y,x,d = map(int,input().split())
    g[y-1][x-1][0].append(d-1)
shy, shx = map(int ,input().split()); shy, shx = shy-1, shx-1


def fishswim(g, smell, shy, shx) :
    ret = deque()
    for y in range(4):
        for x in range(4):
            while g[y][x][0] :
                d = g[y][x][0].popleft()
                yy, xx, dd = -1,-1, -1
                for p in range(8):
                    nd =  8+(d-p) if d-p < 0 else d-p
                    ny,nx = dir[nd][0]+y, dir[nd][1]+x
                    if ny<0 or nx<0 or ny>=4 or nx>=4: continue
                    if smell[ny][nx] or ( shy == ny and shx == nx ) : continue
                    yy, xx, dd  = ny, nx, nd; break
                if yy == -1: ret.append((y,x,d)) # 다음 갈 곳 못찾음
                else: ret.append((yy,xx,dd)) # 다음 갈 곳 찾음
    return ret

sdir = [(-1,0), (0, -1), (1,0), (0,1)] # 상 좌 하 우
def shark_pos(y, x, g, pre, cnt, st, visit):
    global sharkdir, fishcnt
    if len(st) == 3:
        if fishcnt < cnt : fishcnt = cnt; sharkdir = st
        elif fishcnt == cnt and sharkdir > st: fishcnt = cnt; sharkdir = st
        return 
    for i in range(4):
        ny,nx = y+sdir[i][0], x+sdir[i][1]
        if ny<0 or nx<0 or ny>=4 or nx>=4: continue

        if visit[ny][nx] : shark_pos(ny, nx, g, i, cnt, st+str(i), visit)
        else:
            visit[ny][nx] = True
            shark_pos(ny, nx, g, i, cnt+len(g[ny][nx][0]), st+str(i), visit)
            visit[ny][nx] = False
        


for SS in range(S):
    
    # 물고기 복제
    for y in range(4):
        for x in range(4): 
            if g[y][x][0] : g[y][x][1] = g[y][x][0].copy()

    # 물고기 이동
    fish_pos = fishswim(g, smell, shy, shx) 
    for f in fish_pos:
        y,x,d = f
        g[y][x][0].append(d)

    # 상어 이동 칸 구하기
    sharkdir, fishcnt = '999', 0
    visit = [[False]*4 for _ in range(4)]
    shark_pos(shy, shx, g, -1, 0, '', visit)
    
    # 상어 이동 + 물고기 냄새 업데이트
    y, x = shy, shx
    for s in sharkdir:
        d = int(s)
        ny,nx = y+sdir[d][0], x+sdir[d][1]
        if g[ny][nx][0]: g[ny][nx][0] = deque(); smell[ny][nx] = 3
        y,x = ny,nx
    shy, shx = y ,x 
    
    for y in range(4):
        for x in range(4):
            if smell[y][x]>0 : smell[y][x] -= 1

    # 물고기 복제 완료
    for y in range(4):
        for x in range(4):
            if g[y][x][1]: g[y][x][0].extend( g[y][x][1].copy() ) ; g[y][x][1] = deque()
    
print(sum(  len(g[y][x][0]) for x in range(4) for y in range(4)  ))