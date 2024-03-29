from collections import defaultdict,deque
import heapq as hq
INF = float('inf')


n,m,d,e = map(int, input().split()) 
#주환이의 거리 비례 체력 소모량 d, 높이 비례 성취감 획득량 e
distance = [INF] * (n+1)
back = [INF]*(n+1)
h = [-1]+[*map(int, input().split())]
g = [[]for _ in range(n+1)]

for i in range(m):
    a,b,cost = map(int ,input().split())
    g[a].append((b,cost))
    g[b].append((a,cost))

def dijk(s, dist):
    q = []
    dist[s] = 0
    hq.heappush(q,(0,s))
    while q:
        nowcost, now = hq.heappop(q)
        if nowcost > dist[now]: continue
        for l in g[now]:
            nextt, c = l
            if nowcost + c < dist[nextt] and h[nextt]>h[now]:
                dist[nextt] = nowcost + c
                hq.heappush(q, (nowcost + c, nextt))

ans = -float('inf')
dijk(1,distance)
dijk(n,back)

for i in range(1,n+1):
    if distance[i] == INF or back[i] == INF: continue
    ans = max(ans, h[i]*e - distance[i]*d -back[i]*d)
print("Impossible" if ans ==-float("inf")  else  ans)