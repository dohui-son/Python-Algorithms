# 통과했지만 레퍼런스보고 시간 줄이는 공부가 필요

import sys; from collections import defaultdict, deque #인구이동
reader = sys.stdin. readline
ans = 0; total = 0; dir = [(0,1),(1,0),(0,-1),(-1,0)]

n, L, R = map(int,reader().split())
g = [ list(map(int,reader().split())) for _ in range(n)]



def bfs(sy,sx,visit):
    global total,g,dir
    ret = False
    arr = []; q = deque(); visit[sy][sx] = True; q.append((sy,sx))
    while q:
        y,x = q.popleft(); total+= g[y][x]; arr.append((y,x))
        for d in dir:
            ny = y+d[0]; nx = x+d[1]
            if ny<0 or ny>=n or nx<0 or nx>= n:continue
            if visit[ny][nx]: continue
            if L<= abs( g[ny][nx] - g[y][x]) and abs( g[ny][nx] - g[y][x])<=R:
                visit[ny][nx] = True; q.append((ny,nx)); ret = True

    if ret: return arr
    else :
        visit[sy][sx] = False
        return []

while True:
    dq = deque(); countdq = deque()
    visit = [[False]*n for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if visit[i][j] == False:
                tmp = 0
                if i+1<n:
                    if visit[i+1][j] == False and  L<= abs( g[i][j] - g[i+1][j]) and abs( g[i][j] - g[i+1][j]) <=R:
                        tmp +=1
                if j+1<n:
                    if visit[i][j+1] == False and  L<= abs( g[i][j] - g[i][j+1]) and abs( g[i][j] - g[i][j+1]) <=R:
                        tmp +=1
                if tmp>0:
                    total = 0
                    arr = bfs(i,j,visit)
                    dq.append( arr ); countdq.append(total)


    if len(dq) == 0: break
    while dq:
        arr = dq.popleft(); totalnum = countdq.popleft()
        arrlen = len(arr)
        res = totalnum//arrlen
        for i in range(arrlen):
            y,x = arr[i]
            g[y][x] = res
    ans+=1

print(ans)