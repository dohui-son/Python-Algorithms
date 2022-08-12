def solution(A):
    n = len(A)
    if n<=3: return 0
    left = [0]*n
    right = [0]*n
    for i in range(1, n-1): left[i] = max(0, left[i-1]+A[i]) # 단순한 것 같지만 특별한 아이어디였음
    for i in range(n-1,0,-1): right[i-1] = max(0, right[i]+A[i-1])
    ans = 0
    for i in range(1, n-1): ans = max(ans, left[i-1]+right[i+1])
    return ans