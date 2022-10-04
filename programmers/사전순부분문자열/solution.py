from collections import defaultdict, deque
import heapq as hq

def solution(s):
    n = len(s)
    dq = deque()
    q = []
    for i in range(n-1, -1, -1):
        hq.heappush(q, s[i])
        try:
            if q[-1] >= dq[0]:
                dq.appendleft(q[-1])
                del q[-1]
        except: 
                dq.appendleft(q[-1])
                del q[-1]
        
    return ''.join(dq)