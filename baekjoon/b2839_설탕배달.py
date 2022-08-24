n = int( input().rstrip() )
maxfive = n//5
if maxfive:
    for f in range(maxfive,-1,-1):
        rest = n-f*5
        maxthree = rest//3
        if f*5 + maxthree*3 == n: print(f+maxthree);exit(0)
    print(-1)
else:
    if n%3==0: print(n//3)
    else: print(-1)