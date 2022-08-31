# 1시간 31분
from collections import defaultdict, deque
from copy import deepcopy

global shyy,shxx, fish, shdd,ans

# 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다.
fish = defaultdict(list) # y, x, dir
dir = [(-1,0), (-1,-1), (0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
#       0 ↑,     1   ↖,   2 ←,   3 ↙,   4 ↓,  5 ↘, 6 →,   7↗

shyy,shxx,shdd,ans = 0,0,0,0
gg = [[0]*4 for _ in range(4)]
for f in range(4):
    l = [*map(int,input().split())]
    idx = 0
    for i in range(0,8,2):
        num,di = l[i],l[i+1]

        if f == 0 and i == 0: shdd = di-1; ans = num; idx+=1;continue
        fish[num] = [f,idx,di-1]
        gg[f][idx] = num
        idx += 1

tonum = defaultdict(int)
for i in range(1,17): tonum[(1<<i)] = i
alive = (1<<17)-1
alive &= ~(1<<0)
alive &= ~(1<<ans)


def BT(nowalive, kans, shy,shx,shd, fishfish,gg) :
    global ans
    ans = max(ans, kans)

    fnum = nowalive
    g = deepcopy(gg)
    fish = fishfish.copy()
    while fnum : # 살아있는 물고기만 이

        num = tonum[ fnum&-fnum ]
        fnum &= (fnum-1)

        y,x,di = fish[num]
        #이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸
        flag,ny,nx,nd = False , 0,0,0
        for i in range(8):
            nd = (di+i)%8
            ny,nx = y+dir[(di+i)%8][0],x+dir[(di+i)%8][1]
            if ny<0 or nx<0 or ny>=4 or nx>=4: continue
            if ny==shy and nx==shx: continue
            flag = True; break

        if flag: #  이동 가능한 칸이 있음
            if g[ny][nx] == 0:
                g[ny][nx] = num;
                g[y][x] = 0
                fish[num] = (ny,nx,nd)
            else:
                othernum = g[ny][nx]
                otherd = fish[othernum][2]

                g[ny][nx] = num;
                fish[num] = (ny, nx, nd)

                g[y][x] = othernum
                fish[othernum] = (y,x,otherd)
    if nowalive:
        hoobo = 0
        for i in range(1, 4):
            ny, nx = shy + dir[shd][0] * i, shx + dir[shd][1] * i
            if ny < 0 or nx < 0 or ny >= 4 or nx >= 4: break
            if g[ny][nx]: hoobo |= (1<<g[ny][nx])

        while hoobo:
            kbit = hoobo&-hoobo
            hoobo &= (hoobo-1)
            knum = tonum[kbit]
            yy, xx,ndd = fish[knum]

            # 해당물고기 죽여본 후 다시 살려야함

            g[yy][xx] = 0
            BT( nowalive&~kbit, kans+knum, yy, xx, ndd, fish, g)
            g[yy][xx] = knum
    return


anstmp = ans

BT(alive, anstmp, shyy, shxx, shdd, fish,gg)
print(ans)