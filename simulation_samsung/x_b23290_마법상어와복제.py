from collections import defaultdict,deque


#(1, 1)이고, 가장 오른쪽 아랫 칸은 (4, 4)
# 둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다.

# 상은 1, 좌는 2, 하는 3, 우는 4로 변환한다. 변환을 모두 마쳤으면,
# 수를 이어 붙여 정수로 하나 만든다. 두 방법 A와 B가 있고,
# 각각을 정수로 변환한 값을 a와 b라고 하자. a < b를 만족하면 A가 B보다 사전 순으로 앞선 것

global shy,shx,g
shy,shx = 0,0
g = [[[[],0] for _ in range(4)] for _ in range(4)] # [물고기 번호 , 냄새]
m, s = map(int , input().split())

sdir = [(-1,0), (0,-1), (1,0), (0,1)] #상은 1, 좌는 2, 하는 3, 우는 4로 변환
#        0       1      2      3
fdir = [(0,-1), (-1,-1), (-1,0), (-1,1),(0,1),(1,1),(1,0),(1,-1)]
#          ←,      ↖,      ↑,      ↗,    →,    ↘,    ↓,     ↙
#          0       1       2       3     4     5     6      7

fish = defaultdict(list)
for i in range(m):
    y,x,d = map(int, input().split())
    fish[i] = [y-1, x-1, d-1]

shy,shx = map(int,input().split())
shy,shx = shy-1,shx-1
tostr = defaultdict(str); tostr[1] = '1'; tostr[2] = '2'; tostr[3] = '3'; tostr[4] = '4'
anti = defaultdict(str)
anti[0] = '3'; anti[3]='2'; anti[1] = '4'; anti[2] = '1'

def bfs():
    global shy, shx, g
    q = deque([[shy,shx,1,0,'']])


    hoobo = [] # 몇칸째 이동중인지 / 잡은 물고기 마리수 / 사전
    while q:

        y,x,cnt,fcnt,st = q.popleft()
        for num, d in enumerate(sdir):
            ny,nx = d[0]+y, d[1]+x
            if ny<0 or nx<0 or ny>=4 or nx>=4 : continue
            if anti[num] in st: continue
            if len(st) == 1:
                if anti[num] == st[0] : continue
            if len(st) == 2:
                if anti[num] == st[0] or anti[num] == st[1]: continue
            if cnt + 1 <= 4:
                ll = [0,0,'']
                ll[0] = cnt + 1
                ll[1] = fcnt + len( g[ny][nx] )
                ll[2] = st + tostr[num + 1]
                if ll[0] == 4 :
                    if hoobo:
                        if hoobo[-1][0] < ll[1] : hoobo[-1][0] = ll[1];hoobo[-1][1] = -int( ll[2] )
                        elif hoobo[-1][0] == ll[1] and hoobo[-1][1] < -int( ll[2] ) : hoobo[-1][1] = -int( ll[2] )
                    else: hoobo.append( [ll[1], -int(ll[2] )] )
                else: q.append( (ny,nx,ll[0],ll[1],ll[2]) )
    if hoobo:
        hoobo.sort(reverse=True)
        return -hoobo[0][1]
    else: print("no hoobo")
fdx = m
sg = [[0]*4 for _ in range(4)]
for _ in range(s):
    # 물고기 이동 - 복제 마법이 시전됨으로 이동후 전에 있던 칸에서 자기를 없애지 않음에
    key = list(fish.keys())

    ffish = defaultdict(list)

    g = [[deque() for _ in range(4)] for _ in range(4)]  # [물고기 번호 비트, 냄새]
    for fnum in fish:
        y,x,sd = fish[fnum]
        nd,ny,nx,flag = 0,0,0,False
        for i in range(8) :
            nd = sd-i
            if nd<0: nd += 8
            ny, nx = y+fdir[nd][0],x+fdir[nd][1]
            if ny<0 or nx<0 or ny>= 4 or nx>=4: continue
            if ( ny==shy and nx==shx ) or sg[ny][nx]>0: continue # 냄새가 있거나 상어칸이
            flag = True; break
        if flag: # 이동 가능한 칸이 있음
            ffish[fdx] = [ny,nx,nd]
            g[ny][nx].append(fdx)
            fdx+=1
        else:
            ffish[fdx] = [y,x,sd]
            g[y][x].append(fdx)
            fdx += 1

    for y in range(4): # 물고기 냄새 없애주
        for x in range(4):
            if sg[y][x] : sg[y][x] -= 1
    togo = bfs()
    y, x = shy, shx
    for i in range( 2, -1, -1 ): # 상어 이동 - ffish에서 죽이기(g에서도 없애) + 물고기 냄새 남기기
        ten = 10**i
        d = togo//ten - 1
        togo %= ten
        ny, nx =  y+sdir[d][0], x+sdir[d][1]
        if g[ny][nx] :
            sg[ny][nx] = 2
            for fnum in g[ny][nx] : del ffish[fnum]
        y,x = ny,nx
    shy,shx = y,x
    fish.update(ffish)

print(len(fish))