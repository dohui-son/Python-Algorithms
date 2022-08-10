def solution(A, B, K):
    # write your code in Python 3.6
    if A==B : 
        if A%K == 0:return 1
        else: return 0
    b = B//K
    a = A//K
    if A%K == 0: return  b-a+1
    else: return b-a 