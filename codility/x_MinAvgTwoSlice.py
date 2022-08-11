# 시간초과를 해결할 아이디어가 나지 않음
# 중요한 아이디어 ----4개항의 최소값은 무조건 2개항의 최소값보다는 크거나 같게 나오게 된다.***********************
def solution(A):
    n = len(A)
    s,av = 0,int(3e9)
    if n == 2: return s
    psum = [0]*(n+1)
    for i in range(1,n+1): psum[i] = psum[i-1] + A[i-1]
    for i in range(n+1):
        if i+2<n+1: 
            if (psum[i+2]-psum[i])/2<av: 
                av = (psum[i+2]-psum[i])/2
                s = i
        if i+3<n+1: 
            if (psum[i+3]-psum[i])/3<av: 
                av = (psum[i+3]-psum[i])/3
                s = i
    return s