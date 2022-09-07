from collections import defaultdict, deque
import sys ; sys.setrecursionlimit(5000); input = sys.stdin.readline

global ans
tonum = defaultdict(int)
n = int( input().rstrip() )
g = [ [*map(int,input().split())] for _ in range(n)]
for i in range(n): tonum[ (1<<i) ] = i
ans = float('inf')

def BT(ateam, cnt, start) : 
    global ans
    if cnt == n//2:
        bteam = ~ateam & ((1<<n)-1)
        s1,s2 = 0,0
        while ateam:
            adx = ateam &-ateam
            bdx = bteam & -bteam
            ateam &= (ateam-1)
            bteam &= (bteam-1)
            anext, bnext =  ateam, bteam
            while anext:
                asmall = anext&-anext
                bsmall = bnext&-bnext
                
                anext &= (anext-1)
                bnext &= (bnext-1) 
                s1 += g[tonum[adx]][tonum[asmall]]
                s1 += g[tonum[asmall]][tonum[adx]]
                s2 += g[tonum[bdx]][tonum[bsmall]]
                s2 += g[tonum[bsmall]][tonum[bdx]]
        ans = min( ans, abs(s1-s2) )
    for i in range(start,n) : BT(ateam | (1<<i), cnt+1, i+1)
BT(0,0,0)
print(ans)