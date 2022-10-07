from collections import defaultdict,deque
n, m = map(int ,input().split())
parent = [i for i in range(n+1)]

def findd(x):
    if x!= parent[x]: parent[x] = findd(parent[x])
    return parent[x]

def union(a, b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb : return
    if aa < bb: parent[bb] = aa
    else: parent[aa] = bb

for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0: union(a, b)
    else:
        if findd(a)==findd(b): print('YES')
        else: print("NO")