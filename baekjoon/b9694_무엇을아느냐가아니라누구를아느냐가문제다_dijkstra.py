from collections import defaultdict,deque
import sys; sys.setrecursionlimit(5000)
input = sys.stdin.readline
import heapq as hq
INF =int(3e9)

global n,m,g,mini,ans
tonum = defaultdict(int)
for i in range(21): tonum[(1<<i)] = str(i)

def djik():
    global n,m,g,mini,ans
    dist = [INF]*m
    people = [[] for i in range(m)]
    q = []; dist[0] = 0; people[0].append(0)
    hq.heappush(q,(0,0))
    while q:
        c, now = hq.heappop(q)
        if c > dist[now]: continue
        for l in g[now]:
            cc, node = l
            cost = cc+c
            if cost < dist[node]:
                dist[node] = cost
                people[node] = people[now].copy()
                if node not in people[node]: people[node].append(node)
                hq.heappush(q,(cost,node))
    mini = dist[m-1]
    return people[m-1]

t = int(input().rstrip())
for tt in range(t):
    n,m = map(int ,input().split())
    g = [[] for _ in range(m)]
    for nn in range(n):
        x,y,c = map(int ,input().split())
        g[x].append((c,y))
        g[y].append((c,x))
    
    mini, ans = INF, 0
    ans = djik()
    st = "Case #" + str(tt+1)+":"
    if mini == INF: print(st +' -1')
    else: print(st,*ans)