def solution(N):
    if bin(N).count('1') < 2 : return 0
    n = N; preidx = -1; ans = 0
    while n:
        small = n&-n
        idx = bin(small)[::-1].index('1')
        if preidx > -1:
            ans = max(ans, idx-preidx-1)
        preidx = idx
        n &= (n-1)
    return ans