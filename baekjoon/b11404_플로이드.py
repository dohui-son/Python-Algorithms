from collections import defaultdict, deque
INF = int(3e9)
n = int(input().rstrip())
m = int(input().rstrip())
g = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, cost = map(int,input().split())
    g[a-1][b-1] = min(cost, g[a-1][b-1])

# 플로이드 와샬
for mid in range(n):
    for s in range(n):
        for e in range(n): g[s][e] = min(g[s][e], g[s][mid] + g[mid][e])
for y in range(n):
    for x in range(n): print( g[y][x] if g[y][x] < INF and y != x else 0, end=" ")
    print()