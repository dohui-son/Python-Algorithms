from collections import defaultdict, deque

def solution(skill, skill_trees):
    ans, pre = 0, 0
    tobit = defaultdict(int)
    preskill = defaultdict(int)

    for idx, s in enumerate(skill):
        tobit[s] = (1<<idx)
        pre |= (1<<idx)
        preskill[s] = pre

    for st in skill_trees:
        now, flag = 0, True
        for s in st:
            if s in skill:
                now |= tobit[s]
                if preskill[s] & now != preskill[s] : 
                    flag = False; break
        if flag : ans += 1

    return ans