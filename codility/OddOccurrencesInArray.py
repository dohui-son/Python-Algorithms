# 시간 복잡도 : O(N) or O(N*log(N))
def solution(A):
    A.sort(); n = len(A)
    pre = A[0];cnt = 1
    if n == 1: return A[0]
    for i in range(1, n):
        if pre != A[i]: 
            if cnt%2 : return pre
            else : cnt = 1; pre = A[i]
        else : cnt+=1   
    return pre