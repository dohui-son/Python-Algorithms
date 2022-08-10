def solution(A):
    n =  len(A)
    if n == 0: return 1
    A.sort()
    if A[0]>1: return 1
    now = 1
    for a in A:
        if now != a: return now
        now+=1
    return now