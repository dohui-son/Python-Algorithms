from collections import defaultdict,deque
# 1시간 50분 # 상어초등학교
#7월 28일

n = int(input().rstrip())
dic = defaultdict(list)
arr = []; friend = [[] for _ in range(n*n+1)]
dir = [(0,1),(0,-1),(1,0),(-1,0)]
hoobo = deque([]) ; g= [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        hoobo.append((i,j))

for i in range(n*n) :
    l = list( map(int, input().split() ) )
    arr.append( l )
    friend[l[0]].extend(l[1:])
    dic[l[0]] = [-1,-1]

for i,ival in enumerate(arr):
    fq = []
    fcnt = 0

    tq = []
    cnt = 0;
    for h in hoobo:
        tmp = 0 ; ftmp = 0; visit = deque([])
        for d in dir:
            ny,nx = h
            ny += d[0]
            nx += d[1]
            if ny<0 or ny>=n or nx<0 or nx>=n : continue
            if g[ny][nx] == 0 : tmp += 1
            elif g[ny][nx] in ival and g[ny][nx] not in visit:
                visit.append( g[ny][nx] ); ftmp+=1;
        if tmp > cnt :
            tq = []
            cnt = tmp;  tq.append( (-tmp,h[0],h[1]) )
        elif tmp == cnt:
            tq.append((-tmp, h[0], h[1]))
        if ftmp > fcnt :
            fq = []
            fcnt = ftmp ; fq.append( (-tmp,h[0],h[1]) )
        elif ftmp == fcnt:fq.append( ( -tmp,h[0],h[1]) )


    if fcnt>0:
        if len(fq)>1: fq.sort()
        fy, fx = fq[0][1], fq[0][2]
        g[fy][fx] = ival[0]; dic[ival[0]] = [fy,fx]; hoobo.remove((fy,fx))
    else:
        if len(tq) > 1: tq.sort()
        yy = tq[0][1];xx = tq[0][2]
        g[yy][xx] = ival[0]
        dic[ival[0]] = (yy, xx)
        hoobo.remove((yy, xx))
ans = 0; manjok = [0,1,10,100,1000]
for i in range(n):
    for j in range(n):
        now = g[i][j]; cnt = 0
        for d in dir:
            ny,nx = i+d[0],j+d[1]
            if ny<0 or ny >= n or nx<0 or nx>=n:continue
            if g[ny][nx]  in  friend[now]: cnt +=1
        ans += manjok[cnt]
print(ans)

