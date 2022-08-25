#42분 시작 -> 59
from collections import defaultdict, deque
global n,m,g,visit
n,m = map(int, input().split())
g = [ input().rstrip() for _ in range(n)]

dir = [(0,1),(1,0),(-1,0),(0,-1)]

def bfs():
    global n,m,g
    visit = [ [0]*m for _ in range(n)]
    q = deque(); visit[0][0] = 1; q.append((0,0))
    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = d[0]+y, d[1]+x
            if ny<0 or nx<0 or ny>=n or nx>=m: continue
            if ny==n-1 and nx == m-1: print(visit[y][x]+1); exit(0)
            if visit[ny][nx]>0 or g[ny][nx] == '0': continue
            visit[ny][nx] = visit[y][x] + 1
            q.append((ny,nx))
bfs()