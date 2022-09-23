from collections import defaultdict, deque
from copy import deepcopy

global n, g, mynum, kan, wall, dir

# INITIALIZE
n = int(input().rstrip())
g = [[*map(int, input().split())] for _ in range(n)]
tonum = defaultdict(int);
for i in range(30 * 30): tonum[(1 << i)] = i
ans = 0
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
four = [(0,0), (0,n//2+1), (n//2+1,0), (n//2+1,n//2+1)]


def makepair(y,x,ny,nx):
    if y<ny : return (y,x,ny,nx)
    elif y>ny:  return (ny,nx,y,x)
    else:
        if x<nx: return (y,x,ny,nx)
        else: return (ny,nx,y,x)

def bfs(sy, sx, idx, visit):
    global n, g, mynum, kan, wall, dir  # mynum 그룹 이루는 숫자 값 / kan 그룹의 칸 수 / wall 두 그룹이 맞닿아있는 변의 수 key 는 두그룹 idx의 튜플(오름차순) val은 맞닿은 변의 좌표 2개를 오름차순 tuple을 원소로 하는 set
    nowcol = g[sy][sx];
    mynum.append(nowcol);
    kan.append(1)
    visit[sy][sx] = idx
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for d in dir:
            ny, nx = d[0] + y, d[1] + x
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue

            if visit[ny][nx] == idx : continue
            if visit[ny][nx] > -1  and g[ny][nx] != nowcol :
                # 벽더해주기
                if visit[ny][nx] > idx: wall[ (idx,visit[ny][nx])].add( makepair(y,x,ny,nx ) )
                else : wall[ (visit[ny][nx], idx )].add( makepair(y,x,ny,nx ) )
            elif g[ny][nx] == nowcol:
                visit[ny][nx] = idx
                kan[-1] += 1
                q.append((ny, nx))

def scoreSetting():
    global n, g, mynum, kan, wall
    visit = [[-1] * n for _ in range(n)]
    idx = 0
    for y in range(n):
        for x in range(n):
            if visit[y][x] == -1: bfs(y, x, idx, visit); idx += 1
    return idx


def antiClockX(pre): # 십자 모양의 경우 통째로 반시계 방향으로 90' 회전
    global n, g
    x = n//2
    for y in range(n) : g[x][y] = pre[y][x] # 세로 갱신
    y = n // 2
    for x in range(n-1,-1,-1): g[n-1-x][y] = pre[y][x]

def clockBox(sy,sx, pre): # 십자 모양을 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90'씩 회전
    global n, g
    nn = ( n//2 if sx==0 else n )
    for py in range(n//2):
        for px in range(n//2): g[sy+px][nn-1-py] = pre[sy+py][sx+px]   # 이부분이 오래 걸렸다

def rotation():
    global n,g
    pre = deepcopy(g)
    antiClockX(pre)
    for l in four : clockBox(l[0], l[1], pre)

for _ in range(4):

    # SCORE CAL SETTING
    mynum = deque()  # 그룹을 이루는 숫자 값
    kan = deque()  # 그룹에 속한 칸의 수
    wall = defaultdict(set)
    total = scoreSetting()  # 그룹 개수 반환

    # CALCULATE SCORE
    # a와 그룹 b의 조화로움은 (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
    for l in wall:
        cnt = len( wall[l] )
        idx1, idx2 = l
        res = (kan[idx1] + kan[idx2]) * mynum[idx1] * mynum[idx2] * cnt 
        ans += res
    if _ < 3: rotation() # 회전

print(ans)