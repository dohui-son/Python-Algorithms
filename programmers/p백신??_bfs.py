from collections import defaultdict, deque
from itertools import combinations, permutations

def solution(m, n, infests, vaccinateds):
    ans, q = 0, deque()
    g = [[0]*n for _ in range(m)]
    for l in vaccinateds: g[l[0] - 1][l[1] - 1] = -1
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for l in infests:
        q.append((l[0] - 1, l[1] - 1))
        g[l[0] - 1][l[1] - 1] = 1
    
    while q:
        y, x = q.popleft()
        for d in dir:
            ny, nx = y + d[0], x + d[1]
            if ny < 0 or nx < 0 or ny >= m or nx >= n: continue
            if g[ny][nx] == -1: continue
            if g[ny][nx]: continue
            g[ny][nx] = g[y][x] + 1
            q.append((ny, nx))

    for y in range(m):
        for x in range(n):
            if g[y][x] == 0: return -1
            elif g[y][x] - 1 >= 0: ans = max(ans, g[y][x] - 1)
            
    return ans