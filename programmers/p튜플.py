from collections import defaultdict, deque

def solution(s):
    ans = []
    tmp = s.lstrip("{{").rstrip("}}").split("},{")
    arr = []
    for ss in tmp: arr.append([*map(int, ss.split(','))]) 
    arr = sorted(arr, key= lambda x: len(x))
    visit = 0
    for a in arr:
        for aa in a:
            if visit & (1<<aa): continue
            visit |= (1<<aa)
            ans.append(aa)
    return ans