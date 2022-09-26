from collections import defaultdict, deque
import heapq as hq

global n, m , k, c, ans, g, wall,jecho
n, m, k, c = map(int, input().split())
g = [[*map(int, input().split())] for _ in range(n)]
ans, wall = 0, -100
tree = defaultdict(int)
for y in range(n):
    for x in range(n):
        if g[y][x] > 0 : tree[(y,x)] = g[y][x]
        elif g[y][x] == -1: g[y][x] = wall

dir = [(-1,0), (1,0),(0,1),(0,-1)]
tonum = defaultdict(int)
jecho = deque()
for i in range(4): tonum[(1<<i)] = i


jdir = [ (-1,-1), (-1,1),(1,1),(1,-1) ]
def findd(): # 제초제 뿌릴곳 찾아주기
    global n, m, k, c, ans, g, wall, jecho
    q = []

    for keyy in tree:
        y,x = keyy[0], keyy[1]
        cnt = g[y][x]

        for d in jdir:
            for kk in range(1,k+1):
                ny,nx = d[0]*kk + y, d[1]*kk + x
                if ny<0 or nx<0 or ny>=n or nx>=n: break
                if g[ny][nx] <= 0 : break
                elif g[ny][nx]>0: cnt +=  g[ny][nx]
        if q:
            if q[0][0] >= -cnt: hq.heappush(q, (-cnt,y,x))
        else: hq.heappush(q, (-cnt,y,x))
    if q: return ( -q[0][0], q[0][1], q[0][2] )
    else: return (0,0,0)

def spray(sy,sx):
    global n, m, k, c, ans, g, wall, jecho
    g[sy][sx] = -(c+1)
    jecho.append((sy,sx))
    del tree[(sy,sx)]
    for d in jdir:
        for kk in range(1,k+1):
            ny, nx = y+d[0]*kk, x+d[1]*kk
            if ny<0 or nx<0 or ny>=n or nx>=n : continue
            if g[ny][nx] == wall: break
            elif g[ny][nx] == 0:
                jecho.append((ny,nx))
                g[ny][nx] = -(c+1); break
            elif g[ny][nx] < 0:
                g[ny][nx] = -(c+1); break
            elif g[ny][nx] > 0:
                jecho.append((ny, nx))
                g[ny][nx] = -(c+1); del tree[(ny,nx)]


for _ in range(m):
    if jecho:
        pre = jecho.copy()
        for l in pre:
            if g[l[0]][l[1]]<0 and g[l[0]][l[1]]> -100: g[l[0]][l[1]] += 1
            if g[l[0]][l[1]] >= 0 : jecho.remove( l )

    keylist = list(tree.keys())

    for keyy in keylist:
        y,x = keyy[0], keyy[1]
        zero, zvisit = 0, 0
        for idx, d in enumerate( dir ):
            ny,nx = y+d[0], x+d[1]
            if ny<0 or nx<0 or ny>=n or nx>=n : continue
            if (ny,nx) in keylist: g[y][x] += 1; tree[(y,x)] += 1
            elif g[ny][nx]>=0:
                zero += 1
                zvisit |= (1<<idx)
        if zero:
            if g[y][x] // zero :
                newtree = g[y][x] // zero
                while zvisit :
                    nextt = zvisit & -zvisit; zvisit -= nextt
                    d = tonum[nextt]
                    g[ y+dir[d][0] ][ x+dir[d][1] ] += newtree
                    tree[( y+dir[d][0], x+dir[d][1] )] += newtree

    kcnt, y, x = findd() # 제초제 뿌릴 곳 찾음
    ans += kcnt
    if _ == m-1: break
    if kcnt : spray(y,x) # -(c+1)만큼 제초제 뿌리기 + 박멸된 나무 ans에 넣어주기
print(ans)