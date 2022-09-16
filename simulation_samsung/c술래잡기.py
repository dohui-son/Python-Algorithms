from collections import defaultdict, deque
# 술래잡기 4시간
# m명의 도망자가 먼저 동시에 움직이고, - 술래와 거리가 3 이하인 도망자만 움직입니다. 도망자의 위치가 (x1, y1), 술래의 위치가 (x2, y2)라 했을 때 두 사람간의 거리는 |x1 - x2| + |y1 - y2|
# 그 다음 술래가 움직이고
# 이렇게 도망자가 1턴 그리고 이어서 술래가 1턴 진행하는 것을 총 k번 반복

global n, m, h, k, dom, g,ans,eaten,visit,suly, sulx
n, m, h, k = map(int, input().split())
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
sdir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
Kan = deque();
tmp = 0
for i in range(n * 2 - 1):
    if i % 2 == 0 and tmp<n-1: tmp += 1
    Kan.append(tmp)
visit = []

dom = defaultdict(list)
tree = [[False] * n for _ in range(n)]
g = [ [[] for _ in range(n)] for _ in range(n)]
ans, suly, sulx, sd, rev = 0, n // 2, n // 2, 0, False

for mm in range(m):
    y, x, d = map(int, input().split())
    dom[mm] = (y - 1, x - 1, d)
    g[y - 1][x - 1].append(mm)
for hh in range(h):
    y, x = map(int, input().split())
    tree[y - 1][x - 1] = True

def domanga(sy,sx,num):
    global n, m, h, k, dom, g, ans,visit, suly, sulx

    y,x, d= dom[num]
    ny,nx = y+dir[d][0], x+dir[d][1]
    if ny<0 or nx<0 or ny>=n or nx>=n:
        d = (d+2)%4
        ny, nx = y + dir[d][0], x + dir[d][1]
    if suly == ny and sulx==nx : ny,nx = y,x

    if ny!=y or nx!= x:
        g[sy][sx].remove(num)
        g[ny][nx].append(num)
    dom[num] = (ny,nx,d)

def eat(sy,sx,kk):
    global n, m, h, k, dom, g,ans, suly, sulx
    eaten = 0
    for num in g[sy][sx]:
        del dom[num]
        eaten+=1
    g[sy][sx] = []
    ans += kk*eaten

kdx = 0
kan = Kan[kdx]

for kk in range(k):
    # 도망갈 애들만 도망가
    kl = list(dom.keys())
    for keyy in kl:
        y,x,d = dom[keyy]
        if abs(y-suly)+abs(x-sulx)<=3 : domanga(y,x,keyy)

    # 술래 이동후 바로 술래 이동각도 조절
    kan -= 1
    ny,nx = 0,0
    if rev: ny, nx = suly + sdir[sd][0], sulx + sdir[sd][1]
    else: ny, nx = suly + dir[sd][0], sulx + dir[sd][1]

    if kan == 0 or (ny == 0 and nx == 0) or (ny == n // 2 and nx == n // 2):
        if (ny == 0 and nx == 0):
            sd = 0; rev = True; kdx = len(Kan)-1; kan = Kan[kdx]
        elif (ny == n // 2 and nx == n // 2):
            sd = 0; rev = False; kdx = 0; kan = Kan[kdx]
        else:
            sd = (sd + 1) % 4
            if rev : kdx -= 1;kan = Kan[kdx]
            else : kdx += 1;kan = Kan[kdx]
    suly,sulx = ny,nx


    for i in range(0,3):
        if rev:
            ny,nx = suly+sdir[sd][0]*i, sulx+sdir[sd][1]*i
        else:
            ny, nx = suly + dir[sd][0] * i, sulx + dir[sd][1] * i

        if ny<0 or nx<0 or ny>=n or nx>=n: break
        if tree[ny][nx] : continue
        if g[ny][nx] : eat(ny, nx, kk+1)
    if len(dom) == 0: break
    gg = [[1]*n for _ in range(n)]
    gg[suly][sulx] = 0

print(ans)