import math
from collections import defaultdict, deque

def solution(l, v):
    n = len(v)
    v = sorted(v)
    s = v[0] if v[0] else 0
    if v[-1] < l: s = max(s, l - v[-1])
    for i in range(n-1):
        s = max( math.ceil( (v[i+1]-v[i]) /2), s )
    return s