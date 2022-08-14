def solution(A):
    A.sort()
    ans = float('inf')
    n = len(A)
    if n == 1: return abs(A[0])*2
    s,e = 0, n-1
    for a in A: ans = min(abs(a)*2, ans)
    if ans == 0: return ans
    while s<e:
        res = abs(A[s]+A[e])
        if res < ans : ans = res
        if ans == 0: return 0
        if A[s]+A[e]<0: s+=1
        else: e-=1
    return ans