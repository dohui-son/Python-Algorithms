from collections import defaultdict,deque
def solution(cachSize, cities):
    if cachSize == 0: return len(cities)*5
    dq = deque(); ans = 0
    for c in cities:
        cc = c.lower()
        if cc in dq: 
            ans+=1; 
            dq.remove(cc)
        else:
            if len(dq) == cachSize : dq.popleft(); 
            ans+=5
        dq.append(cc) ; 

    return ans