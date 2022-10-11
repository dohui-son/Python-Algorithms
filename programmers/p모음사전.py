from collections import defaultdict, deque
from itertools import combinations
global se
se = set()
def BT(cnt, st, s):
    if st: se.add(st)
    if cnt == 5: return
    for i in range(0, 5): BT(cnt+1, st + s[i], s)

def solution(word):
    global se
    s = ['A','E','I','O','U']
    BT(0,'',s)
    arr = list(se)
    arr.sort()
    return arr.index(word)+1