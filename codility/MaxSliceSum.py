#  O(N)
from collections import defaultdict
def solution(A):
    n = len(A) ;  maxi = max(A); mini = min(A); total = sum(A)
    if n == 1: return A[0]
    if maxi<=0: return maxi
    if mini>=0: return total
    ans = maxi if maxi>total else total
    psum = [0]*(n+1)
    dic = defaultdict(int)
    dic[A[0]] = 0; smallest = [0]*(n+1) # smallest[i] 0번째부터 i번째 psum중에 가장 작은 값을 저장 
    for i in range(1,n+1):
        psum[i] = psum[i-1]+A[i-1]
        smallest[i] = min(smallest[i-1], psum[i])
        dic[psum[i]] = i
    ans = max(max(psum),ans)
    B = psum.copy()
    B.sort(reverse=True)
    ans = max(ans, max(psum))
    for b in B:
        if dic[b] == 0 : continue
        if b - smallest[dic[b]-1]  > ans and dic[b]> dic[b]-1 : ans = b - smallest[dic[b]-1]
    return ans