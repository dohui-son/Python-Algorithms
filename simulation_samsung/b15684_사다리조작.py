# 사다리 조작 1시간 14분
from collections import defaultdict, deque

INF = int(1e9)
global n,m,h, ans, all, hlen

ans, all = INF, 0
n,m,h = map(int, input().split())

hoobo = [ (i,j) for j in range(n-1) for i in range(h) ]
sadari = [ [False]*(n-1) for _ in range(h) ]

for _ in range(m):
    y,x = map(int, input().split()) ; y,x = y-1 , x-1 #b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다
    sadari[y][x] = True
    if x>0: hoobo.remove((y,x-1))
    hoobo.remove((y, x))
hlen = len(hoobo)

def play():
    global n, m, h, ans, all, hlen
    for i in range(n):
        y,x = 0,i
        while y<h:
            y += 1
            if x>0 and sadari[y-1][x-1] :
                x-=1; continue
            if x < n-1 and  sadari[y-1][x] :
                x += 1; continue
        if x != i: return False
    return True

def BT(cur, cnt):
    global n, m, h, ans, all, hlen
    if cnt <= 3 and cnt<ans  :
        if play() and ans>cnt: ans = cnt
        if ans == 0: print(0); exit(0)
    if cnt<3:
        for i in range(cur, hlen):
            sadari[hoobo[i][0]][hoobo[i][1]] = True
            BT(i+1, cnt+1)
            sadari[hoobo[i][0]][hoobo[i][1]] = False


BT(0,0)
if ans == INF : print(-1)
else: print(ans)