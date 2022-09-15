# 온풍기안녕 4시간
from collections import defaultdict,deque
from copy import deepcopy
#
# 집에 있는 모든 온풍기에서 바람이 한 번 나옴
# 온도가 조절됨
# 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
# 초콜릿을 하나 먹는다.
# 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.

global r,c,k,wall,g, heater


r,c,k = map(int,input().split())
info = [[*map(int,input().split())] for _ in range(r)]
g = [[0]*c for _ in range(r)]
wall = [[0]*c for _ in range(r)]
heater = deque()
check = deque()
dir = [(0,1),(0,-1),(-1,0),(1,0)]
wider = [[2,3],[2,3],[0,1],[0,1]]
minus = deque()
w = int(input().rstrip())
for _ in range(w):                       #   t가 0인 경우 (y, x) (3)와 (y-1, x) (2)사이에 벽
    y,x,t = map(int , input().split())   #   1인 경우에는 (y, x) (1)와 (y, x+1) (0)사이에 벽
    y,x = y-1,x-1
    if t == 0:
        wall[y][x] |= (1<<3)
        wall[y-1][x] |= (1<<2)
    else :
        wall[y][x] |= (1<<1)
        wall[y][x+1] |= (1<<0)
for y in range(r):
    for x in range(c):
        if y==0 or x== 0 or y==r-1 or x==c-1: minus.append((y,x))
        if info[y][x] == 5: check.append((y,x));info[y][x] = 0
        elif info[y][x] and g[y][x]<5: heater.append((info[y][x]-1, y, x))



def dfs(pre, d, ondo):
    global r, c, k, wall, g
    visit = [[False]*c for _ in range(r)]
    tmp = [d,*wider[d]]
    now = deque()
    for l in pre:
        ny,nx = 0,0

        for dd in tmp:
            ny,nx = l[0]+ dir[d][0], l[1]+dir[d][1]
            if dd!=d : ny,nx = ny+ dir[dd][0], nx+dir[dd][1]
            if ny<0 or nx<0 or ny>=r or nx>=c: continue
            if visit[ny][nx] : continue
            if dd == d and wall[ny][nx] & (1<<d): continue
            if dd != d and ( wall[ny][nx] & (1<<d) or wall[l[0]+dir[dd][0]][l[1]+dir[dd][1]] & (1<<dd) ) : continue
            g[ny][nx] += ondo
            now.append((ny,nx))
            visit[ny][nx] = True

    if ondo>1: dfs(now, d, ondo-1)

def heat():
    global r, c, k, wall, g,heater
    for l in heater:
        num, y,x = l
        ny,nx = dir[num][0]+y, dir[num][1]+x
        if ny<0 or nx<0 or ny>=r or nx>= c: continue
        if wall[ny][nx] & (1<<num):  dfs(deque([(ny,nx)]), num, 4); continue
        g[ny][nx] += 5
        dfs(deque([(ny,nx)]), num, 4)


def controller():
    global r, c, k, wall, g
    pre = deepcopy(g)
    visit = [[False]*c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if pre[y][x]:
                for idx,d in enumerate(dir):
                    visit[y][x] = True
                    ny,nx = y+d[0], x+d[1]
                    if ny<0 or nx<0 or ny>=r or nx>=c: continue
                    if wall[ny][nx] & (1<<idx): continue
                    if visit[ny][nx]: continue
                    chai = int(abs(pre[y][x] - pre[ny][nx]) / 4 - (abs(pre[y][x] - pre[ny][nx]) / 4)%1)
                    if chai :
                        if pre[y][x] > pre[ny][nx] :
                            g[y][x] -= chai
                            g[ny][nx] += chai
                        else:
                            g[y][x] += chai
                            g[ny][nx] -= chai

def corner():
    for l in minus:
        if g[l[0]][l[1]]:g[l[0]][l[1]]-=1


ans = 0
for tt in range(1,102):
    ans = tt
    if ans == 101: break
    heat()
    controller()
    corner()

    flag = True
    for l in check:
        if g[l[0]][l[1]]<k:flag = False;break
    if flag: break
print(ans)