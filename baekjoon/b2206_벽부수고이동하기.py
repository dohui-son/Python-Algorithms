from collections import defaultdict,deque
global n,m,g
n,m = map(int ,input().split())
g = [input() for _ in range(n)]
INF = int(3e9)
dir = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(sy,sx):
    global n,m,g
    v = [[[0]*2 for _ in range(m)] for _ in range(n)]
    v[sy][sx][0] = 1
    q = deque([(sy,sx,0)])
    while q:
        y,x,bomb = q.popleft()
        if y==n-1 and x == m-1: return v[y][x][bomb]
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=m: continue
            
            if g[ny][nx] == '1' and bomb == 0:
                v[ny][nx][1] = v[y][x][0]+1
                q.append((ny,nx,1))
            elif g[ny][nx] == '0' and v[ny][nx][bomb] == 0:
                v[ny][nx][bomb] = v[y][x][bomb]+1
                q.append((ny,nx,bomb))
    return -1
print(bfs(0,0))