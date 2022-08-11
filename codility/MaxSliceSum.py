# 틀림 수정 필요


#  non-empty array A
# 0 ≤ P ≤ Q < N
from collections import defaultdict
def solution(A):
    n = len(A) #항상 0보다 큼
    if n == 1: return A[0]
    maxi = max(A); mini = min(A)
    if maxi<=0: return maxi
    total = sum(A)
    ans = maxi if maxi>total else total
    if mini>=0: return ans
    psum = [0]*(n+1)
    dic = defaultdict(int)
    dic[A[0]] = 0; smallest = [0]*(n+1); smallest[0] = A[0] 
    for i in range(1,n+1):
        psum[i] = psum[i-1]+A[i-1]
        smallest[i] = min(smallest[i-1], psum[i])
        dic[psum[i]] = i
    B = psum.copy()
    B.sort(reverse=True)
    ans = max(ans, max(psum))
    for b in B:
        if b - smallest[dic[b]-1]  > ans and dic[b]> dic[b]-1 : ans = b - smallest[dic[b]-1]
    



    return ans