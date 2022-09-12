from collections import defaultdict, deque
from itertools import combinations
def solution(number):
    ans,n = 0, len(number)
    combi = list(combinations(number,3))
    for c in combi:
        if c[0]+c[1]+c[2] == 0: ans+=1
    return ans
