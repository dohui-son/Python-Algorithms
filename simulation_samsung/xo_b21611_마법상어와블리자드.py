from collections import defaultdict, deque

global n, m, g, tonum, toyx, shy, shx, ball, ans

ans = 0
n, m = map(int, input().split())
g = [[*map(int, input().split())] for _ in range(n)]
magic = [[*map(int, input().split())] for _ in range(m)]
tonum = defaultdict(int)
toyx = defaultdict(list)
shy, shx = n//2, n//2
ball = deque()

def initialize():
    global n, m, g, tonum, toyx, shy, shx, ball, ans
    dir = [(0,-1), (1,0),(0,1),(-1,0)]
    y, x, cnt, idx, d = shy, shx, 1, 0, 0
    while len(ball) < n**2 - 1:
        for _ in range(2):
            kan = cnt
            while kan:
                ny, nx = y+dir[d][0], x+dir[d][1]
                ball.append(g[ny][nx])
                tonum[(ny, nx)] = idx
                toyx[idx] = (ny,nx)
                g[ny][nx] = idx ### for check
                idx += 1
                if ny==0 and nx == 0: return
                kan -= 1
                y, x = ny, nx
            d = (d+1)%4
        cnt += 1
        if cnt >= n: cnt = n-1
initialize()

def destroyballs(d, lenn):
    global n, m, g, tonum, toyx, shy, shx, ball, ans
    dir = [(-1,0), (1,0),(0,-1), (0,1)] # ↑, ↓, ←, →
    for plus in range(1, lenn+1):
        y, x = shy+dir[d][0]*plus, shy+dir[d][1]*plus
        num = tonum[(y,x)]
        ball[num] = -1

def bomb():
    global n, m, g, tonum, toyx, shy, shx, ball, ans
    pre = ball.copy()
    ball = deque()
    tmp, cnt, ret, rest = deque(), 1, True, True
    for i in range(len(pre)):
        if pre[i] <= 0: continue

        if not tmp: tmp.append(pre[i])
        elif pre[i] != tmp[-1]:
            if cnt >= 4:
                ans += tmp[-1] * cnt # 점수 기록
                ret = False
            else: ball.extend(tmp*cnt)
            tmp = deque([pre[i]])
            cnt = 1
        else: cnt += 1

    if cnt>= 4:
        ans += tmp[-1] * cnt  # 점수 기록
        ret = False
    else: ball.extend(tmp*cnt)

    return ret

def newball():
    global n, m, g, tonum, toyx, shy, shx, ball, ans
    pre = ball.copy()
    ball = deque()
    for i in range(len(pre)):

        if len(ball) > n**2-1: break
        if pre[i] <= 0: continue
        if ball:
            if pre[i] == ball[-1]: ball[-2] += 1; continue
        ball.extend([1,pre[i]])
    while len(ball) > n**2-1: ball.pop()

for mm in magic:
    destroyballs(mm[0]-1, mm[1])
    while True:
        if bomb(): break
    newball()
    if len(ball) < n**2-1 :ball.extend([0]*(n**2-1-len(ball)) )
print(ans)