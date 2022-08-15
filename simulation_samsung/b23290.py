from collections import deque, defaultdict
from copy import deepcopy
dir = [(0,-1),(-1,-1), (0,-1),(1,-1),(0,1),(1,1),(0,1),(-1,1)]
M,S = map(int,input().split())
fish = deque();
arr = [ list(map(int, input().split())) for _ in range(M)]
shy,shx = map(int,input().split())
for ll in range(M):
    y,x,dd = arr[ll]
    y-=1;x-=1;dd-=1
    fish.append([y,x,dd])


nams = defaultdict(int)
sdir = [(-1,0), (1,0),(0,-1),(0,1)]
if len(fish) ==0 : print(0); exit(0)


def shark(g):
    global shy,shx, sdir
    nd,maxi = 0,0
    for idx,d in enumerate(sdir):
        cnt = 0
        tmp = 0
        for i in range(1,4):
            yy,xx = shy+d[0]*i, shx+d[1]*i
            if yy<0 or xx<0 or yy>=4 or xx>=4: break
            tmp += len(g[yy][xx])
            cnt +=1
        if cnt==3 and maxi<tmp:
            maxi = tmp
            nd = idx
    return nd


for __ in range(S):
    ff = deepcopy(fish)
    fflen = len(ff)
    g = [[[] for _ in range(4)] for _ in range(4)]
    for fff in range(fflen) :
        if len(ff) == 0:break
        y,x,dd = ff.popleft()
        ny,nx,nd = y,x,dd
        flag = False
        for i in range(8):
            nd = (dd-i)%8
            if nd < 0 : nd = 8 + nd
            ny,nx = y+dir[nd][0],x+dir[nd][1]
            if ny<0 or nx<0 or ny>=4 or nx>=4: continue
            if ny == shy and nx == shx: continue
            if nams[(ny,nx)]>0: continue
            flag = True;break
        if flag == False: continue
        g[ny][nx].append(nd)
        ff.append([ny,nx,nd])
    #상어 갈길 정하기
    nd = shark(g)
    if len(nams):
        for item in nams:
            if nams[item] > 0: nams[item]-=1
    for i in range(1,4):
        yy,xx = shy+sdir[nd][0]*i, shx+sdir[nd][1]*i
        nams[(yy,xx)] = 2
        print(yy,xx)
        if len(g[yy][xx])>0:
            for j in g[yy][xx] :
                ff.remove([yy,xx,j])
    shy,shx = shy+sdir[nd][0]*3, shx+sdir[nd][1]*3
    fish.extend(ff)
print( len(fish) )









