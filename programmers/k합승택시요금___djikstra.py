from collections import defaultdict, deque
import heapq as hq


def dijk(g,s,n):
    INF = int(3e9)
    ret = [INF] *(n+1) 
    q = []; hq.heappush(q,(0,s))
    ret[s] = 0
    while q:
        nowc, now = hq.heappop(q)
        if nowc>ret[now]: continue
        for l in g[now]:
            node,c = l
            cost = c+nowc
            if cost < ret[node]:
                ret[node] = cost
                hq.heappush(q,(cost,node))
                
    return ret
    

def solution(n, s, a, b, fare):
    ans = 0
    g = [deque() for _ in range(n+1)]
    for f in fare:
        aa,bb,c = f
        g[aa].append((bb,c))
        g[bb].append((aa,c))
    cost =dijk(g,s,n)

    mini = cost[a]+cost[b]
    
    acost = dijk(g,a,n)
    bcost = dijk(g,b,n)
    for i in range(1,n+1):
        if i == s : continue
        mini = min(mini, cost[i]+acost[i]+bcost[i])
    
    return mini