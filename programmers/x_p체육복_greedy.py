from bisect import bisect_left
from collections import defaultdict, deque

def solution(n, lost, reserve):
    ans, visit, arr = 0, 0, []
    for l in lost:
        if l in reserve: reserve.remove(l); lost.remove(l)
    lost.sort()
    reserve.sort()
    
    se = set()
    for num in lost:
        cnt = 0
        dq = deque()
        if num in reserve: 
            idx = reserve.index(num)
            dq.append(idx)
            cnt += 1
        if num-1 in reserve:
            idx = reserve.index(num-1)
            dq.append(idx)
            cnt += 1
        if num+1 in reserve:
            idx = reserve.index(num+1)
            dq.append(idx)
            cnt += 1
        if cnt: arr.append([cnt, dq])
    arr.sort()
    visit = 0
    for l in arr:
        cnt, dq = l
        for num in dq:
            if visit&(1<<num): continue
            ans += 1
            visit |= (1<<num)
            break
    return ans + n-len(lost)