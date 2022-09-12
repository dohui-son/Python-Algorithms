import sys; reader = sys.stdin.readline
from collections import defaultdict, deque
from itertools import combinations, permutations
sys.setrecursionlimit(5000)

n, t = map( int,reader().split() )
g = [[] for _ in range(n)]
for y in range(n):
    for x in range(n) : g[y].append([*map(int,input().split())])

ans = 1
visit = [ [0]*n for _ in range(n) ]

visit[0][0] |= (1<<0)
q = deque([(0,0,0,0)])
dir = [(-1,0),(0,1),(1,0),(0,-1)] # 상0 우1 하2 좌3
shinho = [(0,1,2), (3,0,1),(0,2,3),(1,2,3),   (0,1),(0,3),(2,3),(1,2),   (1,2),(0,1),(0,3),(2,3) ]
#.           1.      2.      3.      4.        5.   6.    7.     8.        9.    10.  11.    12

maxi = 0
cango = [0]*4
cango[0] |= (1<<1);cango[0] |= (1<<5);cango[0] |= (1<<9)
cango[1] |= (1<<0);cango[1] |= (1<<4);cango[1] |= (1<<8)
cango[2] |= (1<<3);cango[2] |= (1<<7);cango[2] |= (1<<11)
cango[3] |= (1<<2);cango[3] |= (1<<6);cango[0] |= (1<<10)
while q:
    if ans == n*n:  break
    y,x,nowd,time = q.popleft()
    dd =  g[y][x][time%4] - 1

    if (1<<dd) & cango[nowd] :
        for d in shinho[dd]: 
            ny,nx = y+dir[d][0], x+dir[d][1]
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if time+1<=t:
                if visit[ny][nx] & (1<<d): continue
                if visit[ny][nx] == 0 : ans+=1
                visit[ny][nx] |= (1<<d)
                
                q.append((ny,nx, d, time+1))

print(ans)