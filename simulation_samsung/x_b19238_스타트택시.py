from collections import defaultdict,deque
global n, m , fuel,g,sonn, ty,tx,sdx

n, m, fuel = map(int, input().split())
g = [ [*map(int, input().split()) ] for _ in range(n)]
ty, tx = map(int, input().split()); ty,tx = ty-1,tx-1
sonn = deque()
dir = [(0,1),(1,0),(-1,0),(0,-1)]
for i in range(m):
    a,b, aa, bb = map(int, input().split())
    a,b,aa,bb = a-1,b-1,aa-1,bb-1
    g[a][b] = i+2
    sonn.append((a,b,aa,bb))
ans, sdx = 0,0


def sbfs():
    global n, m, fuel, g, sonn, ty, tx, sdx
    visit = [[0]*n for _ in range(n)]
    visit[ty][tx] = 1; q = deque(); q.append((ty,tx))
    nq = [];
    sdx = -1

    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if g[ny][nx] == 1 or visit[ny][nx]: continue

            if g[ny][nx]>1 and  visit[y][x]<fuel : nq.append([visit[y][x], ny, nx ]) #시간초과나면 여기 수정해주
            visit[ny][nx] = visit[y][x]+1
            #if visit[ny][nx] > fuel+2: sdx = -1; return -1;
            q.append((ny,nx))
    if nq:
        nq.sort()
        sdx = g[nq[0][1] ][nq[0][2]]-2
        return nq[0][0]
    else : return int(2e9)

def dbfs(dy, dx):
    global n, m, fuel, g, sonn, ty, tx, sdx
    visit = [[0]*n for _ in range(n)]
    visit[ty][tx] = 1; q = deque(); q.append((ty,tx))

    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if g[ny][nx] == 1 or visit[ny][nx]: continue

            if ny==dy and nx == dx:
                if visit[y][x]<=fuel : return visit[y][x]
                else: return int(2e9)
            visit[ny][nx] = visit[y][x]+1
            q.append((ny,nx))
    return int(2e9)


for _ in range(m):
    fuel -= sbfs() #손님 못태워다주면 -1을
    if fuel <= 0:print(-1);exit(0) #손님 태워다주기 실패
    else: ty,tx = sonn[sdx][0], sonn[sdx][1]
    usedfuel = dbfs(sonn[sdx][2],sonn[sdx][3])
    if fuel-usedfuel < 0: print(-1);exit(0)  # 손님 태워다주기 실패
    else:
        fuel += usedfuel
        g[ sonn[sdx][0] ][ sonn[sdx][1] ] = 0
        ty, tx = sonn[sdx][2], sonn[sdx][3]
        ans+=1

print(fuel) if ans == m else -1