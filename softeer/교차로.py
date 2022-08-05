# 시간초과 남
import sys; reader = sys.stdin.readline
from collections import defaultdict,deque
from sys import setrecursionlimit
setrecursionlimit(5000)
INF = int(2e9)
n = int(reader().rstrip())
arr = [ list(reader().split()) for _ in range(n)]
dic=defaultdict(str)
dic[0] = 3
dic[3] = 2
dic[1] = 0
dic[2] = 1
tonum = defaultdict(int)
tonum['A'] = 0
tonum['B'] = 1
tonum['C'] = 2
tonum['D'] = 3
ans = [-1]*n

frr = [[] for _ in range(4)]
mint = int(2e9)
maxt = 0
for ldx, l in enumerate(arr):
    sec, a = l
    sec = int(sec)
    mint = min(sec,mint)
    maxt = max(sec,maxt)
    frr[ tonum[a] ] .append((sec,ldx))
for f in frr: f.sort(reverse= True)

curt = mint
while frr[0] or frr[1] or frr[2] or frr[3]:
    mini = [INF]*4
    for i in range(4):
        if frr[i] :  mini[i] = frr[i][-1][0]
    if mini[0] >= curt and mini[1] >= curt and mini[2] >= curt and mini[3]>= curt : 
        curt = min( min(mini), curt)
    possible = [False]*4
    stuck = [False]*4
    for i in range(4):
        if frr[i]:
            if len(frr[dic[i]]) == 0 and frr[i][-1][0] <= curt:
                possible[i] = True 
            if frr[dic[i]]:
                if frr[dic[i]][-1][0] > curt and frr[i][-1][0] <= curt:
                    possible[i] = True 
            if not possible[i] and frr[i][-1][0] <= curt:
                stuck[i] = True
    if not False in stuck: break
    for i in range(4):
        if possible[i] : ans[frr[i][-1][1]] = curt; frr[i].pop()
    curt+=1
print(*ans, sep="\n")