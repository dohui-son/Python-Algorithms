from collections import  defaultdict, deque

global r,c,m, shark,g, ans

# INITIALIZE
ans = 0
shark = defaultdict(list)
dir = [ (-1,0), (1,0), (0,1), (0,-1)] # 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
r, c, m = map(int ,input().split())
g = [[0]*c for _ in range(r)]
for mm in range(m):
    y, x, s, d, z = map(int ,input().split()) # s는 속력, d는 이동 방향, z는 크기
    shark[z] = (y-1, x-1, s, d-1)
    g[y-1][x-1] = z

# (1) 한칸 이동후 낚시하기
def fishing(x):
    global r, c, m, shark, g, ans
    for y in range(r):
        if g[y][x] :
            keyy = g[y][x]
            g[y][x] = 0
            del shark[keyy]
            ans += keyy
            return

# (2) 상어 이동 - 이동후 잡아먹기
def swim(sy,sx,sp,sd):
    global r, c, m, shark, g, ans # 0인 경우는 위, 1인 경우는 아래, 2인 경우는 오른쪽, 3인 경우는 왼쪽
    kan,y,x,d = sp, sy, sx,sd

    if d < 2  : kan %= (r-1)*2 # 중요한 부분********************
    else : kan %= (c-1)*2
    while kan:
        ny,nx = y+dir[d][0]*kan, x+dir[d][1]*kan
        if ny<0 or nx<0:
            if ny<0: kan -= y; y = 0; d = 1
            else: kan -= x; x = 0; d = 2
        elif ny >= r or nx >= c:
            if ny >=r : kan -= (r-1-y); y = r-1; d = 0
            else: kan -= (c-1-x); x = c-1; d = 3
        else: y,x = ny,nx; kan = 0

    return (y,x,d)


def sharkswim():
    global r, c, m, shark, g, ans
    sizeList = list( shark.keys() )

    for siz in sizeList:
        y, x, sp, sd = shark[siz]

        ny,nx,nd = swim(y,x,sp,sd)
        if g[ny][nx] >0 and g[ny][nx] > siz  : # 나 잡아먹힘
            del shark[siz]
            continue
        elif g[ny][nx] >0 and g[ny][nx] < siz  : # 먼저 온 애 잡아먹기
            del shark[ g[ny][nx] ]
        g[ny][nx] = siz
        shark[siz] = (ny,nx,sp,nd)

for person_x in range(c):
    fishing( person_x)
    g = [[0]*c for _ in range(r)]  # 중요한 아이디어********
    sharkswim()
print(ans)