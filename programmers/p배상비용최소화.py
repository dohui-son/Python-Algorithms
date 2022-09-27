from collections import defaultdict, deque
import heapq as hq

def solution(no, works):
    ans, q = 0, []
    
    for w in works: hq.heappush(q,-w)
    
    for _ in range(no):
        if q[0] == 0: continue
        now = -hq.heappop(q)
        hq.heappush(q, -(now-1) )

    for w in q:
        ans += (-w)**2

    return ans