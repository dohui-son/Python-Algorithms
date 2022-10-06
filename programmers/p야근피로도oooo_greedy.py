from collections import defaultdict, deque
import heapq as hq

def solution(n, works):
    ans, q = 0, []
    for w in works: hq.heappush(q, -w)
    for _ in range(n):
        if q[0] < 0: hq.heapreplace(q, q[0]+1)
    
    return sum(w**2 for w in q)
