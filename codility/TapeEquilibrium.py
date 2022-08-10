def solution(A):
    n = len(A)
    if n == 2: return abs( A[1] - A[0] )
    total = sum(A); ans = 1000*100000
    a = 0
    for i in range(n-1):
        a += A[i] 
        b = total-a
        ans = min(ans, abs(a-b))
    return ans