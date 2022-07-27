import sys; reader = sys.stdin.readline
n = int( reader())
arr = [ list( map(int,reader().split()) ) for _ in range(n) ]
dp = [0]*n; total = 0; ans = float('inf')
for i in range(n):
    for j in range(n): dp[i]+=(arr[i][j]+arr[j][i]); total +=arr[i][j]
def rec(cnt,start,val):
    global ans
    ans = min(abs(val),ans)
    if cnt == n//2: return
    for i in range(start,n):
        rec(cnt+1,i+1,val-dp[i])
rec(0,0,total)
print(ans)