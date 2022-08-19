from collections import deque, defaultdict
#테트로미노 - 1시간 49분
global n,m,ans
n,m = map( int, input().split() )
g = [ [*map(int, input().split())] for _ in range(n) ]
ans = 0

two = [ [ (0,0),(1,0),(2,0),(2,1) ],[(0,0),(0,1),(0,2),(1,0)],[(0,0),(0,1),(1,1),(2,1)],[ (0,1),(1,1),(2,1),(2,0)],    [ (0,0),(1,0), (1,1),(2,1) ],[(0,1),(1,1),(1,0),(2,0)] ,      [ (0,0),(1,0),(2,0),(1,1) ], [(0,1),(1,1),(2,1),(1,0)] ]

def sero(sy,sx):
    global n, m, ans
    for ll in two:
        cnt, tmp = 0, 0
        for yx in ll:
            ny,nx = sy+yx[0],sx+yx[1]
            if ny<0 or nx<0 or ny>=n or nx>=m: break
            cnt+=1 ; tmp+= g[ny][nx]
        if cnt == 4 and ans<tmp: ans = tmp


def garo(sy,sx):
    global n, m, ans
    for ll in two:
        cnt, tmp = 0, 0
        for yx in ll:
            ny,nx = sy+yx[1],sx+yx[0]
            if ny<0 or nx<0 or ny>=n or nx>=m: break
            cnt+=1 ; tmp+= g[ny][nx]
        if cnt == 4 and ans<tmp: ans = tmp



for y in range(n):
    for x in range(m):
        if y+1<n and x+1<m and g[y][x]+g[y+1][x]+g[y][x+1]+g[y+1][x+1] > ans : ans = g[y][x]+g[y+1][x]+g[y][x+1]+g[y+1][x+1]
        if x+3<m and g[y][x]+g[y][x+1]+g[y][x+2]+g[y][x+3]>ans : ans = g[y][x]+g[y][x+1]+g[y][x+2]+g[y][x+3]
        if y+3<n and g[y][x] + g[y+1][x]+g[y+2][x] + g[y+3][x] > ans: ans = g[y][x] + g[y+1][x]+g[y+2][x] + g[y+3][x]
        garo(y,x)
        sero(y,x)
print(ans)