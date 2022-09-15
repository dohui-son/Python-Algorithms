from collections import defaultdict, deque

def solution(s):
    ans = []
    ss = s.lstrip("{{").rstrip("}}").split('},{')
    arr = [ [*map(int,l.split(","))] for l in ss]
    arr.sort(key=len)
    for l in arr:
        for num in l:
            if not num in ans: ans.append(num)
    
    return ans