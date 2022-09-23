from collections import defaultdict, deque
import sys; sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, k = map(int, input().split())
f = [*map(int,input().split())]
g = [[] for _ in range(n+1)]
child = [[i] for i in range(n+1)]
fee = []
ans = 0
parent = [i for i in range(n+1)]


def findd(x):
    if x != parent[x]: parent[x] = findd(parent[x])
    return parent[x]

def union(a,b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb : return
    if aa < bb : 
        tmp = child[ bb ]
        for i in tmp : parent[i] = aa
        child[aa].extend(child[bb])
        child[bb] = []
    else:
        tmp = child[bb]
        for  i in tmp: parent[i] = bb
        child[bb].extend(child[aa])
        child[aa]= []


for _ in range(m):
    a,b = map(int,input().split())
    if a== b: continue
    if not b in g[a] : 
        g[a].append(b)
        union(a,b)
    if not a in g[b] : 
        g[b].append(a)
        union(a,b)
    



for i in range(n) : fee.append((f[i],i+1))
fee.sort()




def unionZero(a,b):
    aa = 0
    bb = findd(b)
    if bb == 0: return False
    else:
        tmp = child[ parent[bb] ] 
        for num in tmp : parent[num] = 0

    return True


for l in fee:
    cost, idx = l
    if unionZero(0, idx) : ans += cost
if max(parent) > 0 or ans>k: print("Oh no")
else: print(ans)