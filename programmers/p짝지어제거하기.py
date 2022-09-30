from collections import defaultdict, deque

def solution(s):
    ans = 0
    dq = deque()
    
    for ss in s:
        try: 
            if dq[-1] == ss: dq.popleft()
        except: dq.append(ss)
    
    return 0 if dq else 1