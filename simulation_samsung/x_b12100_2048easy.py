#2048 (Easy)
from collections import defaultdict, deque
from copy import deepcopy

global n, ans
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값

ans = 2
n = int(input().rstrip())
g = [[*map(int,input().split())] for _ in range(n) ]
for i in g: ans = max( ans,max(i) )



dir = [(0,1),(0,-1),(-1,0),(1,0)] # 다음 확인할 블록 좌표 아는 - 내부 for

fdir = [(1,0), (1,0), (0,1), (0,1)] #
syx = [(0,0), (0,n-1),(n-1,0),(0,0)]



def play(g, dd):
    global ans
    visit = [[False]*n for _ in range(n)] #이동한 자리 기준 좌표 ! 합쳐질 시 합쳐졌다고 true

    for nn in range(n):
        sy, sx = syx[dd][0] + nn * fdir[dd][0], syx[dd][1] + nn * fdir[dd][1]
        # 시작하는 위치 셋팅

        y,x = sy,sx
        for _ in range(n-1) :
            ny, nx = dir[dd][0] + y, dir[dd][1] + x
            found = False # 이 줄 더이상 안 봐도 되는지 알려줌

            while ny>=0 and nx>=0 and ny<n and nx<n :
                if g[ny][nx] : found = True ; break
                ny, nx = ny+dir[dd][0], nx+dir[dd][1]




            if found == False : break # 이 줄은 더이상 볼 필요 없
            else: # 다른 애 찾음
                if g[y][x] > 0:
                    if visit[y][x] == False and g[y][x] == g[ny][nx]:
                        visit[y][x] = True
                        g[y][x] *= 2
                        ans = max(ans, g[y][x])
                        g[ny][nx] = 0
                    else:
                        g[ dir[dd][0] + y ][ dir[dd][1] + x ] = g[ny][nx]
                        g[ny][nx] = 0
                else: # 내가 0일때
                    g[y][x] = g[ny][nx]
                    g[ny][nx] = 0
                    if y!= sy and x != sx: # 나보다 먼저 와서 자리잡은 직전애 확인해주
                        if visit[ y - dir[dd][0] ][ x - dir[dd][0] ] == False :
                            if g[ y - dir[dd][0] ][ x - dir[dd][0] ] == g[y][x]:# g
                                g[y - dir[dd][0]][x - dir[dd][0]] *= 2
                                visit[y - dir[dd][0]][x - dir[dd][0]] = True
                                ans = max( g[y][x]*2 , ans )
                                g[y][x] = 0


            y, x = dir[dd][0] + y, dir[dd][1] + x

def BT(idx, pre, g):
    if idx == 5 : return
    elif idx < 5 :
        for nowd in range(4):
            gg = deepcopy(g)
            play(gg, nowd )
            BT(idx+1, nowd, gg )
BT(0,-1,g)
print(ans)