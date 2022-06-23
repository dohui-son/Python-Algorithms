import sys #수열 #psum (prefix sum)   연속적인 K일의 온도의 합이 최대
reader = sys.stdin.readline
n, k = map( int , reader().split() )
arr = list( map(int, reader().split()))
arr.insert(0,0)
psum = [0]*(n+2)
for i in range(1,n+1):
    psum[i] = arr[i] + psum[i-1]
    
ans = -int(1e9)
for i in range(k, n+1):
    if ans < psum[i]-psum[i-k]:
        ans = psum[i]-psum[i-k]
print(ans)

