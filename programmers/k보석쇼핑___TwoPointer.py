from collections import defaultdict

def solution(g):
    answer = []
    kind = len(set(g))
    s,e,now = 0, 0, 0
    ans = [1,len(g)]
    gem = defaultdict(int); now
    for s in range(len(g)):
        while now < kind and e<len(g):
            gem[g[e]] += 1
            if gem[g[e]] == 1: now +=1
            e+=1
        if now == kind and ans[1]-ans[0] > e-s-1: ans = [s+1,e]
            
        gem[g[s]] -= 1
        if gem[g[s]] == 0: now -= 1
    
    return ans