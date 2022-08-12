def solution(N, P, Q):
    n = N+1
    m = len(P); ans = [0]*m
    p  = [0,0]+[1]*~-n
    for i in range(int(n**.5)+1):
        if p[i]: p[i*i::i] = [0]*(n//i-i+1)
    pp = [2]+[ i for i in range(3, n+1,2 ) if p[i] ]
    plen = len(pp)
    nrr = [False]*n
    for i in range(plen):
        if pp[i]*pp[i]>N:break
        else: nrr[pp[i]*pp[i]] = True
        for j in range(i+1,plen):
            if pp[i]*pp[j]>N: break
            nrr[pp[i]*pp[j]] = True
    psum = [0]*(n)
    for i in range(1,n): psum[i] = psum[i-1]+1 if nrr[i] else psum[i-1]
    for i in range(m):
        ans[i] = psum[Q[i]]-psum[P[i]-1]
    return ans