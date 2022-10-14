from collections import defaultdict, deque
import math
mini, maxi = map(int, input().split())
ans = 0
for i in range(mini, maxi+1): 
    print(i, i**.5) 
    if (i**.5)%1 > 0: ans += 1
print(ans)