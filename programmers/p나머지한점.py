from collections import defaultdict

def solution(v):
    ans = [0,0]
    y = defaultdict(int)
    x = defaultdict(int)
    
    for vv in v:
        y[vv[0]] += 1
        x[vv[1]] += 1
    for k in y:
        if y[k] == 1: ans[0] = k
    for k in x:
        if x[k] == 1: ans[1] = k
        
    return ans