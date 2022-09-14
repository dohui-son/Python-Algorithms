def solution(n):
    memo = [0,1,2]+[0]*n
    for i in range(3,n+1) : memo[i] = memo[i-1]+memo[i-2]

    return memo[n]%1234567

# 도희 숏코딩
def solution(n):
    a,b = 0,1
    for i in range(1,n+1) : 
        a, b = b, a+b
        if i == n: return b%1234567
     