# O(N + M) 
def solution(S, P, Q):
    slen = len(S)
    ans = [0]*len(P)
    psum =[[0,0,0,0] for _ in range(1+slen)]

    for i in range(1,slen+1):
        idx = 0
        if S[i-1] == 'C': idx = 1
        elif S[i-1] == 'G': idx = 2
        elif S[i-1] == 'T': idx = 3
        psum[i][0] = psum[i-1][0]
        psum[i][1] = psum[i-1][1]
        psum[i][2] = psum[i-1][2]
        psum[i][3] = psum[i-1][3]
        psum[i][idx]+=1
    for i, p in enumerate(P):
        q = Q[i]
        if p == q: 
            ans[i] = 1
            if S[p] =='C':ans[i] = 2
            elif S[p] =='G':ans[i] = 3
            elif S[p] =='T':ans[i] = 4
        else:
            if psum[q+1][0]-psum[p][0]: ans[i] = 1
            elif psum[q+1][1]-psum[p][1]: ans[i] = 2
            elif psum[q+1][2]-psum[p][2]: ans[i] = 3
            elif psum[q+1][3]-psum[p][3]: ans[i] = 4
    return ans