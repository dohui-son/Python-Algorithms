from collections import Counter,defaultdict
def solution(A):
    n = len(A)
    if n <= 1 : return 0
    if n==2: return 1 if A[0]==A[1] else 0

    dic = Counter(A)
    ans = 0
    biggest = float('-inf'); idx = A[0]

    psum = defaultdict(int)
    for i in range(1,n):
        psum[A[i-1]] += 1
        if psum[A[i-1]] > biggest: 
            biggest = psum[A[i-1]]
            idx = A[i-1]
        if biggest > i/2 and dic[ idx]-biggest > (n-i)/2: ans+=1
    return ans