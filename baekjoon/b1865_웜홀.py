from collections import defaultdict,deque

global n,m,w,e
INF = int(2e9)

def BF(start):
    global n,m,w,e
    dis = [INF]*(n+1)
    dis[start] = 0

    for i in range(n):
        for edge in e:
            now = edge[0]
            nextt = edge[1]
            cost = edge[2]

            if dis[nextt] > cost+dis[now]:
                dis[nextt] = cost+dis[now]
                if i == n-1: return True
    return False


t = int(input().rstrip())
for _ in range(t):
    n,m,w = map(int, input().split())
    e = []
    
    for _ in range(m):
        s,ee,t = map(int, input().split())
        e.append((s,ee,t))
        e.append((ee,s,t))
    for _ in range(w):
        s,ee,t = map(int, input().split())
        e.append((s,ee,-t))
    flag = False
    for  i in range(1,n+1):
        if BF(i): flag = True;break
    if flag: print("YES")
    else: print("NO")