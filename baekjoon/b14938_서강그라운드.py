INF = int(3e9)
n, m, r = map(int, input().split())
g = [[INF]*n for _ in range(n)]
item = [*map(int, input().split())]
ans = 0
for i in range(r):
    a, b, cost = map(int, input().split())
    g[a-1][b-1] = cost
    g[b-1][a-1] = cost

# 플로이드 워셜
for mid in range(n):
    for s in range(n):
        for e in range(n): g[s][e] = min(g[s][e], g[s][mid] + g[mid][e])
for a in range(n):
    items = 0
    for b in range(n):
        if a==b or g[a][b] <= m: items += item[b]
    ans = max(ans, items)
print(ans)