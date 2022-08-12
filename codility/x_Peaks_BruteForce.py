# O(N * log(log(N)))  본인은 prefix sum으로 풀었지만 다른사람은 BruteForce로 풀었는 듯 
# 다른 사람 코드 - https://smecsm.tistory.com/234
def check(k):
    global psum,n
    if k <= 1: return False
    pre = 0
    for i in range(1, n):
        if i*k-1>=n: break
        if psum[i*k-1] - psum[pre] <= 0: return False
        pre = i*k-1
    return True

def solution(A):
    global psum, plen, n
    n = len(A)
    if n<3: return 0
    peak = [0]*n
    psum = [0]*(n)
    plen = 0
    for i in range(1,n-1):
        if A[i-1]<A[i] and A[i]>A[i+1]: peak[i] = 1;plen += 1
        psum[i] = psum[i-1]+peak[i]
    psum[n-1] = psum[n-2]
    if plen <= 1: return plen
    arr = [n]
    for i in range(2,n):
        if (n/i)%1 == 0: 
            if i == (n//i): arr.append(i);break
            elif i < (n//i): arr.extend([i, (n//i)] )
            else: break
        elif i**2 > n: break
    ans = 0
    for a in arr:
        if check(a): ans = max( n//a, ans)
    return ans