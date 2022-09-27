# 1시간 30분
from collections import defaultdict, deque
from copy import deepcopy

global n, m , k, g ,team, ans
n, m , k = map(int, input().split())
g = [[*map(int,input().split())] for _ in range(n)]
teamg = deepcopy(g)
team = defaultdict(deque)
tnum, ans = 0, 0
dir = [(0,1),(-1,0),(0,-1),(1,0)]


# INITAILIZE
def initbfs(sy,sx,tnum):
    global n, m, k, g, team, teamg
    team[tnum].append((sy,sx))

    teamg[sy][sx] = tnum+1
    g[sy][sx] = 4

    q = deque([(sy,sx)])
    while q:
        y, x = q.popleft()
        for d in dir:
            ny,nx = y+d[0], x+d[1]
            if ny<0  or nx<0 or ny>=n or nx>= n: continue
            if g[ny][nx] == 2:
                teamg[ny][nx] = tnum+1

                g[ny][nx] = 4
                team[tnum].append((ny,nx))
                q.append((ny,nx)); break
            elif g[ny][nx] == 3 and len(team[tnum])>1:
                teamg[ny][nx] = tnum+1

                g[ny][nx] = 4
                team[tnum].append((ny,nx)); break
for y in range(n):
    for x in range(n):
        if teamg[y][x] == 4: teamg[y][x] = 0
for y in range(n):
    for x in range(n):
        if g[y][x]==1: initbfs(y,x,tnum) ; tnum += 1


# (1) 사람들 이동시키기
def moveteams():
    global n, m, k, g, team, teamg

    for mm in range(m):
        arr = team[mm]
        sy,sx = arr[0]

        for d in dir :
            ny, nx = sy+d[0] , sx + d[1]
            if ny<0 or nx<0 or ny>=n or nx>= n: continue
            if g[ny][nx] == 4 and (ny,nx) != arr[1] :
                team[mm].appendleft((ny,nx))
                yy,xx = team[mm].pop()

                teamg[ny][nx] = mm+1
                if not (yy,xx) in team[mm] : teamg[yy][xx] = 0
                break

# (2) 공던져서 점수 획득
def getscore(four, num): # 어느방향 / 몇번째
    global n, m, k, g, team, teamg, ans
    sy,sx, plus = 0,0, ( 1 if four%3 == 0 else -1)

    if four == 0: sy,sx = num, 0
    elif four == 1 : sy,sx = n-1, num
    elif four == 2 : sy,sx = n-1-num,n-1
    elif four == 3: sy,sx = 0, n-1-num

    for p in range(n):
        y, x = sy + dir[four][0]*p, sx + dir[four][1]*p
        if teamg[y][x]>0:
            tnum = teamg[y][x]-1
            idx = team[tnum].index((y,x))
            ans += (idx+1)**2
            team[tnum].reverse()
            return

def playball(kk):
    global n, m, k, g, team, teamg,ans
    four = ( kk // n ) % 4 # 어느방향에서 던지는지
    num = kk % n
    getscore(four, num)


for kk in range(k):
    moveteams()

    playball(kk)