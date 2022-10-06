def solution(K, A):
    ans, pre = 0, -1
    for  i in range(len(A)):
        if A[i] >= K: 
            ans += 1
            pre = -1
        elif pre == -1: pre = A[i]
        else:
            if pre+A[i] >= K:
                ans += 1
                pre = -1
            else: pre += A[i]
    return ans    