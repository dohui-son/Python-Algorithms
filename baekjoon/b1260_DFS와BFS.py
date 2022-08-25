from collections import defaultdict, deque

ndic = defaultdict(int)
b_num = defaultdict(int)

n, m, v = map(int, input().split())

for _ in range(m):
    a,b = map(int, input().split())
    a,b = a-1, b-1
    ndic[ (1<<a) ] |= (1<<b)
    ndic[ (1<<b) ] |= (1<<a)
    b_num[ (1<<a) ] = a
    b_num[ (1<<b) ] = b

visit = (1<<(v-1))
def dfs( now ) :
    global visit
    print(b_num[now]+1, end=" ")
    nodegroup = ndic[now]
    while nodegroup :
        nextt = nodegroup&-nodegroup
        nodegroup &= (nodegroup-1)
        if nextt & visit: continue
        visit |= nextt
        dfs(nextt )

def bfs(v):
    q = deque([(1<<v)]); visit = (1<<v)
    while q:
        now = q.popleft()
        print(b_num[now]+1, end=" ")
        nodegroup = ndic[now]
        while nodegroup:
            nextt = nodegroup&-nodegroup
            nodegroup &= (nodegroup-1)
            if visit & nextt: continue
            visit |= nextt
            q.append(nextt)

dfs(1<< (v-1) )
print()
bfs(v-1)