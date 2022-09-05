import sys; input = sys.stdin.readline
sys.setrecursionlimit(5000)
from collections import defaultdict,deque

n = int(input().rstrip())
arr = []
rev = []
for i in range(n) : arr.append( [*map(int,input().split())] )
arr.sort()
pre = 0
for i in range(n):
    if arr[i][0] > pre : pre = arr[i][0] + arr[i][1]
    else : pre = pre+arr[i][1]
print(pre)