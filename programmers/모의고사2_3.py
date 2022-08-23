
from collections import defaultdict, deque
import heapq as hq
global garo,sero,n
n = 0
garo,sero, INF = 0,0,int(1e9)
dir = [ (0,1), (1,0),(-1,0),(0,-1)]
def bfs(sy,sx, bit, dis,g):
    global garo,sero

    q = deque(); q.append((sy,sx))
    visit = [[0]*garo for _ in range(sero) ]; visit[sy][sx] = 1
    while q:
        y,x = q.popleft()
        for d in dir:
            ny,nx = d[0]+y, d[1]+x
            if ny<0 or nx<0 or ny>= sero or nx>=garo:continue
            if g[y][x] != g[ny][nx] and visit[ny][nx]<visit[y][x]+1: continue
            elif  g[y][x] != g[ny][nx] and visit[ny][nx]<visit[y][x]: continue

            if (1<<g[ny][nx]-1) & bit:
                if dis[ g[ny][nx]-1 ] == -1: dis[ g[ny][nx]-1 ] = visit[y][x]
                elif dis[ g[ny][nx]-1 ] > visit[y][x] : dis[ g[ny][nx]-1 ] = visit[y][x]
            visit[ny][nx] = visit[y][x]
            if g[ny][nx] != g[y][x]:visit[ny][nx]+=1
            q.append((ny,nx))


# def dijk(start, drr, roads):
#     g = [ [] for _ in range(n) ]
#     for y,r in enumerate(roads):
#         for x,node in enumerate(r):
#             if node == -1: continue
#             for d in dir:
#                 ny,nx = y+d[0],x+d[1]
#                 if ny<0 or nx<0 or ny>=sero or nx>= garo: continue
#                 if roads[ny][nx] != node : g[node-1].append( (roads[ny][nx]-1,1) )

#     q = []; drr[start-1] = 0
#     hq.heappush(q,(0,start-1) )
#     while q:
#         distance, now = hq.heappop(q)
#         if distance > drr[now]: continue
#         for l in g[now]:
#             nextt, w = l
#             cost = distance+w
#             if drr[nextt]>cost:
#                 drr[nextt]=cost
#                 hq.heappush(q, (cost, nextt))

def solution(N, roads, sources, destination):
    global garo,sero, INF,n
    n = N
    ans,garo,sero = [0]*len(sources), len(roads[0]), len(roads)
    dis = defaultdict(int)
    tovisit = 0
    for s in sources : tovisit |= (1<<s-1); dis[s-1]=-1
    for i in range(sero):
        for j in range(garo):
            if roads[i][j] == destination:
                bfs(i,j, tovisit, dis, roads)
    # dis = [INF]*(n+1); 
    # dest = []
    # for y,r in enumerate(roads):
    #     for x,node in enumerate(r):
    #         if node == destination:
    #             roads[y][x] = n

                #dest.append((y,x))

    # for y,r in enumerate(roads):
    #     for x,node in enumerate(r):
    #         for d in dir:
    #             ny,nx = y+d[0],x+d[1]
    #             if ny<0 or nx<0 or ny>=sero or nx>= garo: continue
    #             if roads[ny][nx] != node : g[node-1].append( (roads[ny][nx]-1,1) )
    # for dd in dest:
    #     y,x = dd
    #     roads[y][x] = destination 
    #     dijk(destination, dis,roads)

    
    for sdx,s in enumerate( sources ):
        if s==destination:ans[sdx] = 0
        # if dis[s-1] == INF: ans[sdx] = -1
        # else: 
        ans[sdx] = dis[s-1]
    return ans