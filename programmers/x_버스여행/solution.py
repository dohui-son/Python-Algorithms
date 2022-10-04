from collections import defaultdict, deque

def bfs(y, x, g): 
    visit, q = 0, deque([y])
    if y != x: visit |= (1<<y)

    while q:
        now = q.popleft()
        for node in g[now]:
            if visit & (1 << node): continue
            if node == x: return True
            visit |= (1 << node)
            q.append(node)
    return False
    

def solution(n,signs):
    ans = [i[:]  for i in signs]
    g = [[] for _ in range(n)]
    
    for y in range(n):
        for x in range(n):
            if signs[y][x]: 
                ans[y][x] = 1
                g[y].append(x)
                
    for y in range(n):
        for x in range(n):
            if ans[y][x] == 0: 
                if bfs(y, x, g): ans[y][x] = 1
    return ans