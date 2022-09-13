def solution(n):
    memo = [0,1,1]+[0]*n
    for i in range(3,n+1): memo[i] = memo[i-1]+memo[i-2]

    return memo[n]%1234567


# 다른 플이
def solution(n):
    a,b = 0,1
    for i in range(n): a,b = b,a+b
    return a%1234567