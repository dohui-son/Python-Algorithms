from collections import defaultdict,deque

n, m = map(int,input().split())
info = [[*map(int, input().split())] for _ in range(n)]

virus = deque()
for y in range(n):
    for x in range(m):
        