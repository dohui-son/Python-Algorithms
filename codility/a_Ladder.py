from math import pow
def solution(A, B):
    l = len(A)
    maxi = pow(2,30)
    fibo = [0,1,2]+[0]*(l-2)
    for i in range(3,l+1): fibo[i] = (fibo[i-1]+fibo[i-2])%maxi
    ans = [0]*l
    for i in range(l): ans[i] = int(fibo[A[i]]%pow(2,B[i]))
    return ans

    # ref - https://sustainable-dev.tistory.com/40