
from collections import defaultdict
def solution(topping):
    ans, n, INF = 0, len(topping), float('inf')
    maxi = max(topping)
    arr1 = [0]*maxi; arr2 = [0]*maxi
    cnt1,cnt2 = 0,0
    for i in topping : 
        arr2[i-1]+=1; 
        if arr2[i-1] == 1 : cnt2+=1 

    for idx,i in enumerate(topping):
        arr2[i-1]-=1
        arr1[i-1]+=1
        if arr2[i-1] <= 0 : cnt2-=1
        if arr1[i-1] == 1: cnt1+=1

        if cnt1 == cnt2 and cnt1>0: 
            ans+=1
    
    return ans