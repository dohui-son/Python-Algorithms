# 더 효율적인 로직으로 풀어보기
from collections import defaultdict,deque; import copy
n, q = map(int, input().split())
n2 = 2**n
g = [ list(map(int,input().split())) for _ in range(n2)]
qrr = list( map(int, input().split()) )
visit = [ [False]*n2 for _ in range( n2)]

# 2L × 2L --> 회전 90도
dir = [(-1,0),(1,0),(0,-1),(0,1)]
summ = 0
group = 0


def play( sy, sx, sizee ):
    global g
    start_val = g[sy+sizee-1][sx]; end_val = g[sy][sx]
    y = sy; x = sx; nrr = [0]*sizee; srr = []; srr2 = []
    nrr[0] = g[sy+sizee-1][sx+sizee-1]
    if sx + sizee + 1 >= n2: srr2 = g[sy+sizee-1][sx:]; srr = g[sy][ sx : ]
    else:srr2 = g[sy+sizee-1][sx: sx + sizee ]; srr = g[sy][ sx : sx+sizee]
    for i in range(4):
        if i == 2 : y = sy+sizee-1; x = sx
        if i%2 == 0:# 시작이 가로인 경우
            ssy = sy+sizee-1; ssx = sx+sizee-1
            if i>0 : ssx = sx
            for j in range(sizee):
                nrr[j] = g[ ssy - j][ssx]
                if i == 0: g[ssy - j][ssx] = srr[ sizee-1-j]
                else: g[ssy - j][ssx] = srr2[ sizee-1-j]
        else: #시작이 세로인 경우 1 3
            if i == 3 : nrr[sizee-1] = end_val; nrr[0] = start_val
            ssx = sx; ssy = sy
            if i == 1 : ssy = sy + sizee-1
            for j in range(sizee) : g[ssy][ssx + j] = nrr[j]




def firestorm(sizee):
    for se in range(n2 //sizee):
        y = se * sizee
        for ga in range(n2 // sizee):
            x = ga*sizee
            sy = y; sx = x
            for i in range( sizee // 2): #8 -> 6
                play(sy,sx, sizee -2*i )
                sy += 1;  sx+= 1






for qq in qrr:
    firestorm( 2**qq )


    summ = 0
    before = copy.deepcopy(g)
    for i in range(n2):
        for j in range(n2):
            cnt = 0
            if before[i][j] == 0: continue
            for d in dir:
                ny, nx = i+d[0], j+d[1]
                if ny< 0 or ny>=n2 or nx<0 or nx>=n2 : continue
                if before[ny][nx]>0: cnt += 1
            if cnt < 3 : g[i][j] -= 1
            summ += g[i][j]

def bfs(i,j):
    global dir,visit
    q = deque(); q.append( (i, j) ) ; visit[i][j] = True; cnt = 1
    while q:
        y,x = q.popleft()
        for d in dir:
            ny, nx = y+d[0], x+d[1]
            if ny<0 or ny>=n2 or nx<0 or nx>=n2: continue
            if 0 < g[ny][nx] and visit[ny][nx] == False:
                cnt+=1; visit[ny][nx] = True; q.append((ny,nx))
    return 0 if cnt <= 1 else cnt

for i in range(n2):
    for j in range(n2):
        if visit[i][j] == False and g[i][j] > 0 : group = max(bfs(i, j), group)

print( summ )
print( group )

#남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
