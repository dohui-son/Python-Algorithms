from collections import defaultdict, deque

def solution(progresses, speeds):
    ans, pre,idx = [1], -1, 0

    for p,s in zip(progresses, speeds):
        days = (100-p)//s  + ( 1 if ((100-p)/s)%1>0 else 0 )
        
        if pre>-1 and pre >= days: ans[idx] += 1
        elif pre>-1 : ans.append(1)
        
        if pre < days: pre = days; idx = len(ans)-1
    return ans