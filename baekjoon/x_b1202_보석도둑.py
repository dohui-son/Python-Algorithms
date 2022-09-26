from collections import defaultdict, deque
import heapq as hq

n, k = map(int, input().split())
dia, bag = [], []

for _ in range(n):
    m, v = map(int, input().split())
    dia.append((m,v))
dia.sort()

for _ in range(k) : bag.append( int(input()) )
bag.sort()

idx, q, ans = 0, [], 0
for i in range(k):
    while idx < n and dia[idx][0] <= bag[i]:
        hq.heappush( q, -dia[idx][1] )
        idx += 1
    if len(q) : ans -= hq.heappop(q)
print(ans)