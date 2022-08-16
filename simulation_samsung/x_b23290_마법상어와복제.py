from collections import deque, defaultdict
from copy import deepcopy

M,S = map(int, input().split())
fish = deque()
shy,shx = 0,0

arr = [ list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    y,x,dd = arr[i]; y,x,dd = y-1,x-1,dd-1
    fish.append([y,x,dd])

dir = [(0,-1), (-1,-1), (-1,0),(-1,1), (0,1), (1,1), (1,0), (1,-1)]
smell = defaultdict(int)

sdir = [(-1,-1), (-1,0), (0,-1), (1,0), (0,1) ]
def shark(g):
    global sdir
    maxi, st_dir = 0, 9999999999999999999
    for i in range(1,5):
        ny, nx =  shy+sdir[i][0], shx+sdir[i][1]
        if ny<0 or nx< 0 or ny>=4 or nx>=4: continue
        else:
            visit = [ [False]*4 for _ in range(4)]
            visit[shy][shx] = True
            visit[ny][nx] = True
            cnt = len(g[ny][nx]); tmp = 100*i
            for j in range(1,5):
                ny2, nx2 = ny + sdir[j][0], nx + sdir[j][1]
                if ny2 < 0 or nx2 < 0 or ny2 >= 4 or nx2 >= 4: continue
                if not visit[ny2][nx2]:

                    tmp2 = tmp + 10 * j;
                    cnt2 =  cnt+ len(g[ny2][nx2])
                    visit[ny2][nx2] = True
                    for k in range(1,5):
                        ny3, nx3 = ny2 + sdir[k][0], nx2 + sdir[k][1]

                        if ny3 < 0 or nx3 < 0 or ny3 >= 4 or nx3 >= 4: continue
                        if not visit[ny3][nx3]:

                            cnt3 = cnt2
                            cnt3 += len(g[ny3][nx3]);
                            visit[ny3][nx3] = True
                            tmp3 = tmp2 + k
                            if maxi == cnt3 and tmp3<st_dir : st_dir = tmp3; maxi = cnt3
                            elif maxi<cnt3: st_dir = tmp3; maxi = cnt3
                        visit[ny3][nx3] = False
                visit[ny2][nx2] = False
            visit[ny][nx] = False
    return st_dir

for _ in range(S):
    g = [[[] for _ in range(4)] for _ in range(4)]
    fish2 = deepcopy(fish)
    while fish2:
        y,x,dd = fish2.popleft()
        ny,nx,nd = 0,0, dd
        for i in range(1,9):
            nd  = dd - i
            if nd<0: nd = (nd%8+8)%8
            ny,nx = y+dir[nd][0], x + dir[nd][1]
            if ny<0 or nx<0 or ny>=4 or nx>=4: continue
            if ny == shy and nx == shx: continue
            if smell[(ny,nx)]>0: continue
            break
        if nd == dd: continue
        g[ny][nx].append(nd)
        fish.append([ny,nx,nd])
        print("append", [ny,nx,nd])
    for kkey in smell:
        if smell[kkey]>0: smell[kkey]-=1
    st_dir = str(shark(g))
    idx,ny,nx = 0, shy,shx
    while idx<3:
        nd = int(st_dir[idx])
        ny,nx = ny+sdir[nd][0], nx+sdir[nd][1]
        print(st_dir,idx,"==", nd, "-", ny,nx)
        print(fish)
        if len(g[ny][nx]) > 0:
            for ff in g[ny][nx] :
                smell[(ny,nx)] = 2
                print( [ny,nx,ff] )
                fish.remove([ny,nx,ff])
        idx += 1
    shy, shx = ny, nx
print( len(fish) )




