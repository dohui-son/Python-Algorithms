from collections import defaultdict, deque
global visit, N, M

dir = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(g, color, sy, sx):
    q = deque([ (sy,sx) ])
    while q:
        y,x = q.popleft()
        for d in dir:
            ny, nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if g[ny][nx] == color and visit[ny][nx] == False: 
                visit[ny][nx] = True
                q.append((ny,nx))

def solution(n, m, image):
    global visit, N, M
    visit = [[False]*m for _ in range(n)]
    ans, N, M = 0, n , m
    
    for y in range(n):
        for x in range(m):
            if visit[y][x] == False: 
                visit[y][x] = True
                bfs(image, image[y][x], y, x)
                ans += 1
    return ans