# O(N*log(N))
def solution(A):
    n = len(A)
    if n<=2: return 0
    A.sort()
    if A[n-1] <= 0: return 0
    for i in range(0,n-2):
        if A[i]>0:
            summ = A[i]+A[i+1]
            third = 0
            if A[i] == A[i+1] == A[i+2] and A[i]>0:return 1 
            for j in range(i+2,n):
                if A[j]<A[i]+A[i+1] :return 1
                else: break
    return 0