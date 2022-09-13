# 어항 정리 - 3시간 25
from collections import defaultdict,deque
from copy import deepcopy
global n,k,g,gg
n,k = map(int,input().split())
g = [*map(int,input().split())]
gg = []

def curl():
    global n, k, g
    ret = [[ g[1],g[0] ],[ g[2],g[3] ]]

    now = 4 # 이 인덱스부터는 g어항
    while len(ret) <= ( n-now ):
        pre = deepcopy(ret)
        nn = len(ret)
        mm = len(ret[0])
        ret = [[0]*nn for _ in range(mm+1)]
        yy = 0
        for x in range(mm):
            xx = 0
            for y in range(nn-1,-1,-1):
                ret[yy][xx] = pre[y][x]
                xx+=1
            yy+=1
        idx,i = 0,now
        while idx<nn:
            ret[-1][idx] = g[i]
            idx += 1; i+=1
        now = i
    if now < n-1 : ret[-1].extend(g[now:])

    return ret


dir = [(0,1),(1,0)]
def fish_arrange(gg,g):
    global n, k
    pre = [[-1]*len(gg[-1]) for _ in range(len(gg))]
    nn = len(gg)
    for y in range(nn):
        mm = len(gg[y])
        for x in range(mm): pre[y][x] = gg[y][x]
    mm = len(gg[-1])

    for y in range(nn):
        for x in range(mm):
            if pre[y][x] == -1: continue
            for d in dir:
                ny,nx = y+d[0],x+d[1]
                if ny<0 or ny>=nn or nx<0 or nx>=mm: continue
                if pre[ny][nx] == -1: continue
                chai = abs(pre[y][x]-pre[ny][nx])//5
                if chai :
                    if pre[y][x]>pre[ny][nx] : gg[y][x] -= chai; gg[ny][nx] += chai
                    else:gg[y][x] += chai; gg[ny][nx] -= chai
    idx = 0
    for x in range(mm):
        for y in range(nn-1,-1,-1):
            if pre[y][x] == -1: continue
            g[idx] = gg[y][x]
            idx += 1
    return g
def makeG():
    global n, k, g
    ret = [ g[:n//2][::-1], g[n//2:] ]


    for i in range(n):
        mm = len(ret[0])
        nn = len(ret)
        ret2 = [[0]*(mm//2) for _ in range(nn*2)]

        yy = nn
        for y in range(nn):
            xx = 0
            for x in range(mm//2,mm):
                ret2[yy][xx] = ret[y][x];xx+=1
            yy+=1
        yy = 0
        for y in range(nn-1,-1,-1):
            xx = 0
            for x in range(mm//2-1,-1,-1):ret2[yy][xx]=ret[y][x]  ;xx+=1
            yy+=1

        if len(ret2[i])==n//4: return ret2
        ret = ret2




for time in range(987654321):
    maxi, mini = max(g), min(g)
    if maxi-mini <=k : print(time); exit(0)
    for i in range(n):
        if g[i]== mini: g[i]+=1 # (1) 물고기의 수가 최소인 어항 모두에 한 마리씩 넣는다
    gg = curl()


    g = fish_arrange(gg,g) # 한줄짜리 어항 g업데이트도 끝!!!!


    ggg = makeG()


    g = fish_arrange(ggg,g)


