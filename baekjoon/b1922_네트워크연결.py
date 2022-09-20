from collections import defaultdict,deque

n = int(input().rstrip())
m = int(input().rstrip())
arr = []
for _ in range(m):
    a,b, c = map(int ,input().split())
    arr.append((c,a-1,b-1))
arr.sort()
parent = [i for i in range(n)]

def findd(x):
    if parent[x] != x: parent[x] = findd(parent[x])
    return parent[x]

def union(a,b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb: return False
    elif aa<bb: parent[bb] = aa
    else: parent[aa] = bb
    return True


ans = 0
for l in arr:
    cost,a,b = l
    if union(a,b): ans += cost
print(ans)