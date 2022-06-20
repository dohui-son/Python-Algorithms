import sys #동전 0
reader = sys.stdin.readline
n , k = map(int, reader().split())
ans = 0

arr = list(int( reader().rstrip() ) for _ in range(n)) 
for i in range(n):
        ans += ( k // arr[n-i-1] )
        k %= arr[n-i-1]
    
print(ans)