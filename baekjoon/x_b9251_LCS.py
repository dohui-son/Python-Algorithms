from collections import defaultdict,deque

a = input().rstrip()
b = input().rstrip()
n, m = len(a), len(b)
memo = [[0]*1001 for _ in range(1001)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if b[i-1] == a[j-1]: memo[i][j] = memo[i-1][j-1]+1
        else: memo[i][j] = max(memo[i-1][j], memo[i][j-1])
print(memo[m][n])