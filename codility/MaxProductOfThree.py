def solution(A):
    if min(A)>=0:
        A.sort(reverse=True)
        return A[0]*A[1]*A[2]
    else:
        n = len(A)
        A.sort()
        return A[n-1]*A[n-2]*A[n-3] if A[n-1]*A[n-2]*A[n-3] > A[0]*A[1]*A[n-1] else A[0]*A[1]*A[n-1]