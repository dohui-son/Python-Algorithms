from collections import defaultdict, deque
from bisect import bisect_right
import heapq as hq
INF = int(3e9)

def dijk(g, n, k):
    dis = [INF]*n
    dis[0] = 0
    q = []
    hq.heappush(q, (0,0))
    while q :
        c, now = hq.heappop(q)
        if c > dis[now] or c > k: continue
        for l in g[now]:
            node, nc = l
            cost = nc + c
            if cost <= k and dis[node] > cost:
                dis[node] = cost
                hq.heappush(q,(cost, node))
    return dis 

def solution(N, road, K):
    ans = 0
    g = [[] for _ in range(N)]
    for l in road:
        a, b, cost = l
        g[a-1].append( (b-1,cost) )
        g[b-1].append( (a-1, cost) )
    dist = dijk(g, N, K)

    if min(dist) > K: return 0
    else:
        dist.sort()
        return bisect_right(dist, K)