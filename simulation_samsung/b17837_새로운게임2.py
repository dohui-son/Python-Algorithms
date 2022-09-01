#새로운 게임2 - 40분

from collections import defaultdict, deque

global ans,n,k,mal

INF, ans = int(2e9), 0
dir = [(0,1),(0,-1),(-1,0),(1,0)]
anti = defaultdict(int); anti[0]=1; anti[1] = 0; anti[2]=3;anti[3] = 2
st = defaultdict(str); tonum = defaultdict(int)
#턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
#한 말이 이동할 때 위에 올려져 있는 말도 함께 이동
#말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르

n, k = map(int,input().split())
g = [[*map(int,input().split())] for _ in range(n)]
gg = [[""]*n for _ in range(n)]

mal = defaultdict(list)
for kk in range(k):
    y,x,dd = map(int,input().split())
    mal[kk] = [y-1,x-1,dd-1]
    st[kk] = str(kk); tonum[ st[kk]] = kk
    gg[y-1][x-1] = st[kk]


def check(ny,nx):
    if ny<0 or nx<-0 or ny>=n or nx>=n: return 1
    if g[ny][nx] == 2: return 2
    return 0

def move(sy,sx,dd,num):
    global ans, n, k, mal
    ny,nx = sy+dir[dd][0], sx+dir[dd][1]
    rd = dd
    res = check(ny,nx)
    if res >0 : #지도밖이거나 blue
        ny,nx,rd = sy+dir[anti[dd]][0],sx+dir[anti[dd]][1], anti[dd]
        mal[num][2] = rd
        if check(ny,nx) > 0 : mal[num] = [sy,sx,rd]; return

    slen,idx = len(gg[sy][sx]),0
    for i in range(slen):
        if gg[sy][sx][i] == st[num] : idx = i; break


    now = gg[sy][sx][idx:]
    gg[sy][sx] = gg[sy][sx][:idx]
    if g[ny][nx]:gg[ny][nx] += now[::-1] # 빨강
    else:gg[ny][nx] += now # 화이트
    if len(gg[ny][nx]) >3: print(ans); exit(0)

    for s in now:
        mal[ tonum[s] ][0] = ny
        mal[tonum[s]][1] = nx


for i in range(1, 1001):
    ans = i
    for kk in range(k):
        y,x,dd = mal[kk]
        move(y,x,dd,kk)

print(-1)