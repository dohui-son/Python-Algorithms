# O(N)
#  0 ≤ P ≤ Q < N
# loss of A[P] - A[Q]
#profit  A[Q] - A[P], ->이럴때만 A[Q] ≥ A[P]
from collections import defaultdict
def solution(A):
    n = len(A)
    if n <= 1 : return 0
    maxi = max(A); mini = min(A)
    if maxi == mini:return 0

    if A.index(maxi) > A.index(mini) : return maxi - mini
    psum = [0]*n
    dic = defaultdict(int)
    dic[A[0]] = 0
    for i in range(1,n):
        dic[ A[i] ] = i
        if A[ psum[i-1] ] > A[i]: psum[i] = i
        else: psum[i] = psum[i-1]
    aa = A.copy()
    aa.sort(reverse=True)
    ans = 0

    for a in aa:
        if dic[a] == 0 :continue
        if ans < a - A[ psum[ dic[a]-1 ] ] : ans = a - A[ psum[ dic[a]-1 ] ]     
    return ans 



