from collections import defaultdict, deque
def solution(priorities, location):
    loc = location
    pre = 0
    p = deque(priorities)
    while p:
        if loc != 0:
            if p[0] < max(p): p.rotate(-1)
            else: 
                p.popleft()
                pre += 1
            loc -= 1
        else:
            if p[0] < max(p):
                p.rotate(-1)
                loc = len(p) - 1
            else: return pre + 1 