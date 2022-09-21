from collections import defaultdict, deque

dir = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(g,n):
    INF = int(2e9)
    visit = [[[INF]*4 for _ in range(n) ] for _ in range(n)]
    q = deque() 
    q.append((0,0,0,0))
    q.append((0,1,0,0))
    while q:
        precost,pre,y,x = q.popleft()
        
        for idx, d in enumerate(dir):
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if g[ny][nx] : continue
            cost = precost+1
            if idx%2 != pre%2: cost += 5
            if visit[ny][nx][idx] > cost:
                visit[ny][nx][idx] = cost
                if ny==n-1 and nx==n-1: continue
                q.append((cost,idx,ny,nx))
                
    return visit
           

def solution(g):
    INF = int(2e9)
    n =len(g)
    v = bfs(g,n)
    
    return min(v[n-1][n-1])*100