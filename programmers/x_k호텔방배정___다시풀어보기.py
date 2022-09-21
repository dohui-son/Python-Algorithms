import sys; sys.setrecursionlimit(10000)
from collections import defaultdict

def findEmpty(num, parent):
    if parent[num] == 0:
        parent[num] = num+1
        return num
    nextt = findEmpty(parent[num], parent)
    parent[num] = nextt+1
    return nextt

def solution(k, rn):
    n = len(rn)
    ans = [0] * n
    parent = defaultdict(int)
    
    for num in rn:
        ret = findEmpty(num, parent)

    return list(parent.keys())