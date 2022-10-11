import heapq as hq
from collections import defaultdict, deque
def dijk(n, g):
    INF = int(3e9)
    dist = [INF]*n
    q = []
    dist[0] = 0
    hq.heappush(q, (0,0))
    while q:
        c, now = hq.heappop(q)
        if c > dist[now]: continue
        for node in g[now]:
            if c + 1 < dist[node]:
                dist[node] = c+1
                hq.heappush(q,(c+1, node))
    return dist

def solution(n, edge):
    g = [ deque() for _ in range(n)]
    for l in edge: 
        g[l[0]-1].append(l[1]-1)
        g[l[1]-1].append(l[0]-1)

    dist = dijk(n, g)
    return dist.count(max(dist))