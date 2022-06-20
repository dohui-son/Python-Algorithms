import sys
reader = sys.stdin.readline
n = int( reader().rstrip() )
arr = [(0,0)]*n
ans,s,e =0,0,0

for i in range(n):
    s, e = map(int, reader().split())
    arr[i] = (e,s)
arr.sort()
e = 0
for i in range(n):
    if( e <= arr[i][1] ):
        ans+=1
        e = arr[i][0]
print(ans)
