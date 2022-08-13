# O(N) or O(N * log(N))
def solution(A):
    maxi = max(A); n = len(A)
    if maxi <= 0: return 1
    A.sort(); visit = 1
    ans = 0
    for a in A:
        if a >= 1 and not visit&(1<< a) :
            visit |= (1<<a)
            if a != ans+1: return ans+1
            ans = a
    return maxi+1
