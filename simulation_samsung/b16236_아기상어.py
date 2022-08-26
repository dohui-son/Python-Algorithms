# 아기상어 52분
from collections import defaultdict, deque
global n, shy, shx, siz, ans, m,g


n = int(input().rstrip())
g = [ [ * map(int, input().split())] for _ in range(n)]
shy, shx, siz, ans, m,eaten = 0,0,2,0, 0,0


for y in range(n) :
    for x in range(n) :
        if g[y][x] == 9 : shy = y; shx = x; g[shy][shx] = 0
        elif g[y][x]>0 : m += 1


def eat(fish,g):
    global n, shy, shx, shy, shx,siz, ans, m
    if len( fish ) > 1 : fish.sort();
    g[fish[0][1]][fish[0][2]] = 0;
    shy = fish[0][1]; shx = fish[0][2]
    return fish[0][0]

dir = [ (-1,0), (0,-1), (0,1), (1,0)]

def bfs(g):
    global n, shy, shx, shy, shx, siz, ans, m
    q = deque(); q.append((shy,shx))
    visit = [[0]*n for _ in range(n)]
    visit[shy][shx] = 1
    fish = []
    while q :
        y, x = q.popleft()

        for d in dir:
            ny, nx = d[0]+y, d[1]+x

            if ny<0 or nx<0 or ny>=n or nx>= n: continue
            if visit[ny][nx] > 0 or g[ny][nx]>siz: continue

            if g[ny][nx] > 0 and g[ny][nx]<siz :
                if len(fish) > 0 :
                    if fish[-1][0] <= visit[y][x] : fish.append( [visit[y][x], ny,nx ] )
                    else: time =  eat( fish , g); return time
                else: fish.append( [visit[y][x], ny,nx ] )
            visit[ny][nx] = visit[y][x]+1
            q.append( (ny,nx) )
    if fish: time =  eat(fish,g); return time
    else: return -1

    return -1

for mm in range(m):
    res = bfs(g)
    if res > 0 : eaten += 1; ans += res
    else : break # 물고기 다 잡아먹음

    if eaten == siz : siz += 1; eaten = 0


print( ans )