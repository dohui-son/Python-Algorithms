from collections import defaultdict, deque


def solution(skill, skill_trees):
    tonum = defaultdict(int)

    for i in range(len(skill)) : tonum[skill[i]] = i+1 
    ans = 0
    for sk in skill_trees:
        total,flag = 1, True
        for s in sk:
            if tonum[s]==0: continue
            total |= (1<<tonum[s])
            if (1<<tonum[s])-1 & total != (1<<tonum[s])-1 : flag = False;break
        if flag : ans+=1
    return ans