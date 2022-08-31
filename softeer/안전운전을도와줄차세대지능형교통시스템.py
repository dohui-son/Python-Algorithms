import sys; reader = sys.stdin.readline
from collections import defaultdict, deque
from itertools import combinations, permutations
sys.setrecursionlimit(5000)

n, t = map( int,reader().split() )
g = [[] for _ in range(n)]
for y in range(n):
    for x in range(n) : g[y].append([*map(int,input().split())])

ans = 1
visit = [[0]*n for _ in range(n)]
visit[0][0] = 1
q = deque([(0,0,0)])
dir = [(-1,0),(0,1),(1,0),(0,-1)] # 상0 우1 하2 좌3
shinho = [(0,1,2), (3,0,1),(0,2,3),(1,2,3),   (0,1),(0,3),(2,3),(1,2),   (1,2),(0,1),(0,3),(2,3) ]
#.           1.      2.      3.      4.        5.   6.    7.     8.        9.    10.  11.    12


while q:
    y,x,nowd = q.popleft()
    lenn = len(g[y][x])
    for tt,dd in enumerate(g[y][x]):
        if nowd == 0 and (dd!=2 and dd!=6 and dd!=10):continue
        if nowd == 1 and (dd!=1 and dd!=5 and dd!=9):continue
        if nowd == 2 and (dd!=4 and dd!=8 and dd!=12):continue
        if nowd == 3 and (dd!=3 and dd!=7 and dd!=11):continue
        if tt != (visit[y][x]-1)%(lenn+1): continue
        for d in shinho[dd-1]:
            ny,nx = y+dir[d][0], x+dir[d][1]
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if visit[ny][nx]>0: continue
            visit[ny][nx] = visit[y][x]+1
            if visit[y][x] > t: continue
            ans += 1
            q.append((ny,nx, d))
print(ans)