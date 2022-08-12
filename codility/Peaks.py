# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def check(k):
    global psum,n
    if k == 0: return False
    pre = 0
    for i in range(n//k+1):
        if psum[i*k] - psum[pre]: continue
        else: return False
        pre = i*k
    return True


def solution(A):
    global psum, plen, n
    n = len(A)
    if n<=2: return 0
    peak = [0]*n
    psum = [0]*(n+1)
    plen = 0
    for i in range(1,n-1):
        if A[i-1]<A[i] and A[i]>A[i+1]: peak[i] = 1;plen += 1
        psum[i] = psum[i-1]+peak[i-1]
    psum[n-1] = psum[n-2]+peak[n-2]
    psum[n] = psum[n-1] + peak[n-1]
    s,e = 0, plen+1
    while (s+1 < e):
        mid = (s+e) // 2
        if check(mid) : s = mid
        else: e = mid
    return s