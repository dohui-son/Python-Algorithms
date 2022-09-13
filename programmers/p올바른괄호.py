from collections import defaultdict, deque
def solution(s):
    stk = 0
    
    for ss in s:
        if ss=="(" : stk += 1
        elif ss==")" and stk==0: return False
        else: stk -= 1
    
    return False if stk else True