# 시간 복잡도 : O(N) or O(N*log(N)) - 비트마스킹으로 하니 시간이 O(n**2)나왔엇음...
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