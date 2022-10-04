def solution(d, budget):
    ans, spent = 0, 0
    d.sort()
    for dd in d:
        if spent + dd <= budget: 
            ans += 1
            spent += dd
    return ans