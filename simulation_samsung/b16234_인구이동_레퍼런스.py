# 인구이동문제
# 최단시간 연산



# https://www.acmicpc.net/source/36146931
import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def DFS(x, y):
    global s, cnt
    nQ.append((x, y))
    ch[x][y] = 1
    cnt += 1
    s += gra[x][y]
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<N) or ch[xx][yy] == 1: continue
        if L <= abs(gra[xx][yy]-gra[x][y]) <= R:
            DFS(xx, yy)


N, L, R = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]

Q = deque()
for i in range(N):
    for j in range(N):
        Q.append((i, j))
        
res = 0        
while Q:
    ch = [[0]*N for _ in range(N)]
    for _ in range(len(Q)):
        x, y = Q.popleft()
        if ch[x][y] == 1: continue
        s = 0
        cnt = 0
        nQ = []
        DFS(x, y)
        if cnt == 1: continue
        s = s//cnt
        for a, b in nQ:
            gra[a][b] = s
            Q.append((a, b))
    if not Q: break
    res += 1


print(res)