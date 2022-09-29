from collections import defaultdict, deque
import sys; sys.setrecursionlimit(7000)
global n, ans

def zip_str( num, st):
    global n, ans
    neww, pre, cnt = '', st[:num], 1
    
    for i in range(num, n , num):
        if len(neww) >= ans : return 
        if pre == st[i:i+num] : cnt += 1
        else:
            if cnt>1 : 
                neww += str(cnt) + pre
                cnt = 1
            else:
                neww += pre
            pre = st[i:i+num]
            
    if cnt>1 : neww += str(cnt) + pre
    else : neww += pre
    
    if len(neww) < ans: ans = len(neww) 
    
def solution(s):
    global n, ans
    ans, n = len(s), len(s)
    
    for i in range(1, n-1) : zip_str( i, s )
    
    return ans