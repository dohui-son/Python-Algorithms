from collections import defaultdict, deque
import heapq as hq

def solution(no, works):
    q = []
    
    for w in works: hq.heappush(q,-w)
    
    for _ in range(no):
        if q[0] == 0: continue
        hq.heapreplace(q, q[0]+1 )

    return sum(w**2 for w in q)