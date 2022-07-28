# 마법상어와 비바라기 50분
from collections import deque,defaultdict
dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
n,m = map(int, input().split() ); arr = [[] for _ in range(n)]; mm = []
dlen = len(dir)
for i in range(n):
    arr[i].extend(list(map(int, input().split())))
for j in range(m):
    a, b = map(int, input().split() )
    mm.append((a,b)) #이동의 정보 di, si
dq = deque([])
dq.append([n-1,0]);dq.append([n-1,1]);dq.append([n-2,0]);dq.append([n-2,1]);

def findNext(y,x,d,s):
    yy = (y+dir[d][0] * s)%n
    xx = (x + dir[d][1] * s)%n
    if yy < 0: yy+=n
    if xx < 0: xx+= n
    return [yy,xx]


for i in mm:
    visit = [[False] * n for _ in range(n)]
    d,s = i; d-=1
    dqlen = len(dq)
    for j in range(dqlen): #1, 2번 과정
        dq[j] =  findNext( dq[j][0],dq[j][1], d, s)
        y, x = dq[j]
        visit[y][x] = True
        arr[y][x] += 1
    dic = defaultdict(int)
    while dq:
        y,x = dq.popleft();  cnt = 0
        for i in range(1, dlen, 2):
            yy= y+dir[i][0]
            xx = x+dir[i][1]
            if yy<0 or yy>=n or xx < 0 or xx>=n:continue
            if arr[yy][xx] > 0: cnt+=1
        if cnt>0: dic[(y,x)] = cnt

    for ii in range(n):
        for jj in range(n):
            arr[ii][jj] += dic[(ii, jj)]
            if visit[ii][jj]:continue
            if arr[ii][jj]>=2:
                dq.append([ii, jj])
                arr[ii][jj] -= 2
ans = 0
for i in arr:
    ans += sum(i)
print(ans)


