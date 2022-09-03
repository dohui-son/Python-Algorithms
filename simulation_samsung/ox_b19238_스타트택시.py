from collections import deque, defaultdict
import heapq as hq

global n,m,fuel, ty,tx, dy,dx

n,m,fuel = map(int,input().split())
g = [ [*map(int, input().split())] for _ in range(n)]
ty,tx = map(int, input().split()) ; ty,tx = ty-1, tx-1
start = deque()
end = defaultdict(list)
for _ in range(m):
    a,b,aa,bb = map(int, input().split())
    start.append((a-1,b-1)); end[(a-1,b-1)] = (aa-1,bb-1)

dir = [ (0,1),(1,0),(-1,0), (0,-1)]
def bfs( arr ) :
    global n, m, fuel, ty, tx

    q = []; hq.heappush(q,(0,ty,tx))
    visit = [[False]*n for _ in range(n)]
    visit[ty][tx] = True
    while q:
        cost, y, x = hq.heappop(q)
        if (y,x) in arr : return [cost, y, x]
        for d in dir:
            ny, nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if g[ny][nx]>0 or visit[ny][nx]==True: continue
            visit[ny][nx] = True
            hq.heappush(q,(cost+1,ny,nx))
    return int(2e9), 0,0

for i in range(m):
    dy,dx = 0,0
    used, yy, xx = bfs(start)
    if fuel-used <= 0 : print(-1); exit(0)
    else:
        fuel -= used
        ty, tx = yy, xx
        dy,dx = end[(yy, xx )]

    used, _, _ = bfs( [(dy,dx)] )

    if fuel-used>=0 :
        fuel += used
        start.remove( (yy,xx) )
        ty,tx = dy,dx
    else: print(-1); exit(0)
print(fuel)