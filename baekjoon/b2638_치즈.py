from collections import defaultdict,deque

n,m = map(int,input().split())
g = [[*map(int,input().split())] for _ in range(n)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(g):
    sy,sx = 0,0
    visit = [[0]*m for _ in range(n)]
    se = set()
    q = deque([(0,0)])
    visit[0][0] = True
    ret = True
    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=m: continue
            if g[ny][nx] : 
                visit[ny][nx] += 1; 
                if visit[ny][nx]>=2: se.add((ny,nx)); ret = False
            if visit[ny][nx]: continue
            visit[ny][nx] += 1
            if g[ny][nx] == 0: q.append((ny,nx))
    for l in se : g[l[0]][l[1]] -= 1
    return ret

for i in range(n*m):
    if bfs(g): print(i);exit(0)