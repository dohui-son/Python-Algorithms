# 플로이드 워셜
import sys; input = sys.stdin.readline
from collections import defaultdict, deque
import heapq as hq
global INF,n,g,dist
INF = float('inf')
n = int( input().rstrip() )
g = [[INF]*n for _ in range(n)]
if n == 1: print(0); exit(0)

for i in range(n-1):
    x, y, cost = map(int, input().split() )
    g[x-1][y-1] = cost
    g[y-1][x-1] = cost
dist = [[INF]*n for _ in range(n)]

def FW():
    global INF,n,g,dist
    for i in range(n):
        for j in range(n): dist[i][j] = g[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]: dist[i][j] = dist[i][k] + dist[k][j]
FW()

for i in range(n) : print( sum(dist[i])-dist[i][i] )