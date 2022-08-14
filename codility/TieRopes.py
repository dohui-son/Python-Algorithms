def solution(K, A):
    s,n,e,ans = 0,len(A), 0, 0
    while s<n:
        summ = 0
        while e<n and summ<K:
            summ+=A[e]
            e+=1
        if summ >= K: ans+=1
        s = e
    return an