from collections import defaultdict, deque
import heapq as hq

n = int(input().rstrip())
arr = [] 
for _ in range(n):
    p, d = map(int ,input().split())
    arr.append((d, p))
arr.sort()
ans = []
for l in arr:
    hq.heappush(ans, l[1])
    if len(ans) > l[0] : hq.heappop( ans )

print( sum(ans) )