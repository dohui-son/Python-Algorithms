import sys; reader = sys.stdin.readline
from collections import defaultdict,deque
from sys import setrecursionlimit
setrecursionlimit(5000)
n = int(reader().rstrip())
arr = [ list(reader().split()) for _ in range(n)]
dir = ['A','D','C','B']
dic=defaultdict(str)
dic['A'] = 'D'
dic['D'] = 'C'
dic['B'] = 'A'
dic['C'] = 'B'
tonum = defaultdict(int)
tonum['A'] = 0
tonum['B'] = 1
tonum['C'] = 2
tonum['D'] = 3


frr = [[] for _ in range(4)]

for l in arr:
    sec, a = l
    frr[ tonum[a] ] .append(int(sec))
for f in frr: f.sort()
ans = defaultdict(int)
arr2 = arr.copy()
arr2.sort()
def dp(sec,alpha):
    ret = int(sec)
    if (sec,alpha) in ans : return ans[sec,alpha]
    elif sec in frr[0] and sec in frr[1] and sec in frr[2] and sec in frr[3]: 
        ret = -1
        frr[0].remove(sec); frr[1].remove(sec); frr[2].remove(sec); frr[3].remove(sec) 
    elif ret in frr[ tonum[dic[alpha]] ]:
        ret = max( dp(sec, dic[alpha])+1, ret )
        frr[tonum[alpha]].append(ret)
    ans[(sec,alpha)] = ret
    return ret
for l in arr2 : dp(l[0],l[1])

for l in arr:
    sec, a = l
    print( ans[(sec,a)] )