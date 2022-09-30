from collections import defaultdict, deque
import heapq as hq

def solution(max_weight, specs, names):
    ans = 0
    dic = defaultdict(int)
    for s in specs: dic[s[0]] = int(s[1])
    q, n, now = [], len(names), 0
    for name in names: 
        if now + dic[name] > max_weight:
            now = dic[name]
            ans += 1
        elif now + dic[name] == max_weight:
            now = 0
            ans += 1     
        else: now += dic[name]
        
    return ans + 1 if now else ans