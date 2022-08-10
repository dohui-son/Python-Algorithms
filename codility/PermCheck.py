def solution(A):
    n = len(A)
    if len(set(A)) != n: return 0
    maxi = max(A)
    if n != maxi: return 0
    visit = 1
    for i in A:
        if (1<<i)&visit: return 0
        visit |= (1<<i)
    return 1 if visit == (1<< (maxi+1))-1 else 0