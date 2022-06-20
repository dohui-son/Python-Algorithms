import sys #ATM
reader = sys.stdin.readline
ans = 0

n = int( reader().rstrip() )
arr = list(map(int, reader().split()) )
arr.sort()
for i in range(n):
    ans += (n-i)*arr[i]
print(ans)
