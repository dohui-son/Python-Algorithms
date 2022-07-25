import sys;reader = sys.stdin.readline  
n = int( reader().rstrip() ) ; ans = 1
while n!= 1:
    if (n & 1) : ans+=1 
    n //= 2
print(ans)