from collections import defaultdict, deque
import math
global n,m,t,ans,g
n,m,t = map(int, input().split())
ans = -1
g = []
for nn in range(n):
    l = deque( [*map(int, input().split())] )
    g.append(l)

dir = [(1,0),(0,1),(0,-1),(-1,0)]

def bfs(sy,sx):
    global n, m, t, ans, g
    num = g[sy][sx]
    q = deque(); q.append( (sy,sx) ); g[sy][sx] = 0
    while q:
        y,x = q.popleft()
        for d in dir:
            ny, nx = d[0]+y, d[1]+x
            if ny<0 or ny>=n: continue
            if nx >= m: nx %= m
            if g[ny][nx] == 0 : continue
            if g[ny][nx] == num:
                g[ny][nx] = 0
                q.append( (ny,nx) )

def play(xx, d, k, tt):
    global n, m, t, ans, g
    for idx in range(xx, n, xx+1) :
        g[idx].rotate(d*k)


    done = False
    for y in range(n):
        for x in range(m):
            if g[y][x] == 0:continue
            for d in dir:
                ny,nx = y+d[0], x+d[1]
                if ny<0 or ny>=n : continue
                if nx >= m: nx %= m
                if g[y][x]>0 and g[y][x] == g[ny][nx] :
                    done = True
                    bfs(y,x)


    if done == False :
        cnt, summ, av = 0,0,0
        dq = deque()
        for i,ival in enumerate(g):
            for j,val in enumerate(ival):
                if val>0 :  cnt+=1; summ+=val; dq.append((i,j))
        if cnt>0:
            av = summ/cnt

            for yx in dq:
                y_,x_ = yx
                if g[y_][x_] > av: g[y_][x_] -=1 ; summ-=1
                elif g[y_][x_]<av: g[y_][x_] +=1 ; summ+=1
            if tt == t-1: ans = summ
        else: print(0); exit(0)

for tt in range(t):
    xx,d,k = map(int,input().split())
    dd = 1 if d == 0 else -1
    play(xx-1, dd, k ,tt)

if ans == -1:
    ans = 0
    for i in g: ans += sum(i)
print(ans)