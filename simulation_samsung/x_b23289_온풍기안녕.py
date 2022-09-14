from collections import defaultdict,deque



global r,c,k,origin,heater,g
r,c,k = map(int, input().split())
origin = [ [ *map(int,input().split()) ] for _ in range(r)]  #5: 온도를 조사해야 하는 칸
tester = deque()
heater = deque()
for y in range(r):
    for x in range(c):
        if origin[y][x] == 5: tester.append((y,x)); origin[y][x] = 0
        elif origin[y][x] and origin[y][x]<4 : heater.append((origin[y][x]-1, y,x)); origin[y][x] = 5 # 5는 히터 있는
dir = [(0,1),(0,-1),(-1,0),(1,0)]
anti = defaultdict(int); anti[0] = 1; anti[1] = 0; anti[2] = 3; anti[3] = 2

w = int(input().rstrip())
for ww in range(w):
    y,x,t = map(int,input().split())
    y,x = y-1,x-1
    if t == 0: origin[y][x] = 3; origin[y-1][x] = 4
    else: origin[y][x] = 1; origin[y-1][x] = 2
g = [[0]*c for _ in range(r)]

def dfs( q, d, ondo ): #q에 저번 라인 들어있음
    ret = deque()

    for l in q:
        y,x = l
        ny,nx = dir[d][0]+y, dir[d][1]+x
        if ny<0 or nx<0 or ny>=r or nx>=c: continue
        if origin[ny][nx] == 5: continue
        if origin[y][x] and origin[y][x]-1 == d: continue
        g[ny][nx] += ondo; visit = True
        ret.append((ny,nx))

    tmp = []
    if len(ret)>=2:tmp = [ret[0], ret[-1]]
    # else: tmp = [ret[0],ret[0]]
    for l in tmp:
        y,x = l
        for idx,dd in enumerate(dir):
            if idx == d: continue
            if idx == anti[d]: continue
            ny,nx = y+dd[0],x+dd[1]
            if ny >= 0 and nx >= 0 and ny< r and nx < c:
                if (ny,nx) in ret: continue
                g[ny][nx] += ondo
                if ondo>1:
                    if (y,x) == q[0]: ret.appendleft((ny,nx))
                    else: ret.append((ny,nx))
    if ondo>1: dfs(ret,d,ondo-1)




def heat():
    for h in heater :
        dd, yy,xx = h
        y,x = yy+dir[dd][0], xx+dir[dd][1]
        if y<0 or x<0 or y>=r or x>=c: continue
        g[y][x] += 5
        q = deque([(y,x)])
        visit = [[0]*]
        while q:
            y,x = q.popleft()
            for idx,d in enumerate(dir):


                if idx == dd: g[ny][nx] += (visit[ny][nx]-1)

for _ in range  (1): #(1,102):
    choco = _
    heat()
    for i in g: print(i)
    # heatcontrol()   # 2. 온도조절
    # low()           # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소


    flag = True
    for t in tester:
        if g[t[0]][t[1]] < k: flag = False;break
    if flag: break
print(choco)