from collections import defaultdict, deque
n, m = map(int ,input().split())
height = [[0]*n for _ in range(n)]
for _ in range(m):
    tall, short = map(int, input().split())
    height[tall-1][short-1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1): height[i][j] = 1 # i보다 j가 작은 경우
print(   sum( ( sum( height[i][j]+height[j][i] for j in range(n) ) == n-1 ) for i in range(n) ) )