# 드래곤 커브 - 1시간 36분
from collections import defaultdict, deque
visit = [ [0]*101 for _ in range(101)]
n = int(input().rstrip())
dragon = [ list(map(int,input().split())) for _ in range(n)]

dir = [(0, 1), (-1,0), (0,-1),(1,0)]
for l in dragon:
    sx, sy, dd,sede = l
    dq = [dd]
    visit[sy][sx] = 1; visit[sy+dir[dd][0]][sx+dir[dd][1]] = 1
    y,x = sy+dir[dd][0], sx+dir[dd][1]
    if sede:
        for i in range( sede):
            dqlen = len(dq); tmp = []
            for j in range(dqlen-1,-1,-1):
                nd = ( dq[j] + 1)%4
                tmp.append(nd)
                y,x = y+dir[nd][0],x+dir[nd][1]
                visit[y][x] = 1
            dq.extend(tmp)
ans = 0
for i in range(100):
    for j in range(100):
        if visit[i][j] and visit[i+1][j] and visit[i][j+1] and visit[i+1][j+1]:  ans+=1
print(ans)