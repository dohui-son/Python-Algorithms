from collections import deque,defaultdict #1시간 10분
n,m = map(int, input().split() )
sy, sx, sd = map(int, input().split())
if sd == 1: sd = 3
elif sd == 3 : sd = 1
arr = [ list(map(int,input().split())) for _ in range(n)]

dir = [[-1,0],[0,-1],[1,0],[0,1]]
visit = [[0]*m for _ in range(n)]

def fin():
    ans = 0
    for i in visit : ans += sum(i)
    print(ans); exit(0)

while True:
    visit[sy][sx] = 1 # 지금 자리 청소
    ny,nx,nd = 0,0,0
    flag = True
    for d in range(1,5):
        nd = (sd+d)%4
        ny = sy + dir[nd][0]; nx = sx + dir[nd][1]
        if ny<0 or ny>=n or nx<0 or nx>=m: continue
        if arr[ny][nx] == 1: continue
        if visit[ny][nx] == 0: flag = False; break
    if flag : # 네 방향다 청소 불가능
        by,bx = sy+dir[(sd+2)%4][0], sx+dir[(sd+2)%4][1]
        if by<0 or by>=n or bx<0 or bx>=m : fin()
        elif arr[by][bx] == 1 : fin()
        else: sy = by; sx = bx  # 뒤로 후진 가능이라 후진
    else: # 청소 가능
        visit[ny][nx] = 1
        sd = nd
        sy,sx = ny,nx
fin()