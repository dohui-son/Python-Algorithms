from collections import defaultdict, deque
n = int(input().rstrip())
m = int(input().rstrip())
g = [[*map(int, input().split())]  for _ in range(n)]
plan = [*map(int ,input().split())]
parent = [i for i in range(n)]

def findd(x):
    if parent[x] != x: parent[x] = findd(parent[x])
    return parent[x]

def union(a, b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb: return
    elif aa<bb: parent[bb] = aa
    else: parent[aa] = bb 
    return
for fromm in range(n):
    for to in range(fromm+1,n):
        if g[fromm][to]: union(fromm, to)

for i in range(len(plan)-1):
    if parent[plan[i]-1] != parent[plan[i+1]-1]: print('NO'); exit(0)
print("YES")