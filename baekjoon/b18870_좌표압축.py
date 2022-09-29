from collections import defaultdict,deque
from bisect import bisect_left
n = int(input().rstrip())
arr = [*map(int,input().split())]
ans = [0]*n

g = list(set(arr))
g.sort()
for i in range(n): ans[i] = bisect_left(g, arr[i])
print(*ans)