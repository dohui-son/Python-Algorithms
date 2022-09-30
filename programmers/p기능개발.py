from collections import defaultdict, deque
import math

def solution(progresses, speeds):
    ans, pre,idx = [1], -1, 0

    for p,s in zip(progresses, speeds):
        days = math.ceil((100-p)/s)  
        
        if pre>-1 and pre >= days: ans[idx] += 1
        elif pre>-1 : ans.append(1)
        
        if pre < days: pre = days; idx = len(ans)-1
    return ans