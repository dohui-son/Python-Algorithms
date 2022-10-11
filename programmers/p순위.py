from collections import defaultdict, deque

def solution(n, results):
    ans = 0
    res = [ [set(), set()] for _ in range(n+1)] # [내가 진 애들, 내가 이긴 애들]
    
    for l in results:
        winner, looser = l
        
        for win in res[winner][0]: 
            res[win][1].add(looser)
            res[win][1] |= res[looser][1]
        for lost in res[looser][1]: 
            res[lost][0].add(winner)
            res[lost][0] |= (res[winner][0])
        res[winner][1].add(looser)
        res[winner][1] |= res[looser][1]
        res[looser][0] |= res[winner][0]
        res[looser][0].add(winner)
        
    for s in res:
        if len(s[0]) + len(s[1]) == n-1: ans +=1
    return ans