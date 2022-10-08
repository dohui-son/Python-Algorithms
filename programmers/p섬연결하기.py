global parent, N
parent = [i for i in range(101)]

def findd(x):
    if parent[x] != x: parent[x] = findd(parent[x])
    return parent[x]

def union(a, b):
    aa = findd(a)
    bb = findd(b)
    if aa == bb: return False
    if aa < bb: parent[bb] = aa
    else: parent[aa] = bb
    return True

def solution(n, costs):
    global parent, N
    ans, N = 0, n
    g = sorted(costs, key =  lambda x: x[2])
    for l in g:
        a, b, cost = l
        if union(a,b): ans += cost
    return ans